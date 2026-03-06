import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import numpy as np
import math
# --------------------------------------------------
# 🎨 1. CONFIGURACIÓN GLOBAL (El truco de oro)
# --------------------------------------------------
# Esto hace que TODOS los gráficos nazcan oscuros sin tener que repetirlo
pio.templates.default = "plotly_dark"

st.set_page_config(layout="wide", page_title="Justina BI - Estrategia")

# Solo dejamos el CSS para las tarjetas de los KPIs y el padding, nada de fondos
st.markdown("""
    <style>
        .block-container { 
        padding-top: 45px !important; 
        padding-bottom: 45px !important; 
        max-width: 95% !important; /* Estira el contenedor casi al total de la pantalla */
    }

    h1 {
        font-size: 48px !important; 
        color: #ffffff !important;
        padding-bottom: 20px !important;
        width: 100% !important;
        text-align: center !important;
        white-space: nowrap !important; /* Fuerza a que no salte de línea */
    }
        
        /* --- TARJETAS DE KPIs --- */
        [data-testid="stMetric"], div[data-testid="metric-container"] {
            background-color: #1c2030 !important; 
            border: 1px solid #252a38 !important; 
            padding: 15px 20px !important;
            border-radius: 12px !important;
            box-shadow: 0 4px 10px rgba(0,0,0,0.4) !important;
            border-top: 3px solid #4eb1cb !important;
            display: flex !important;
            flex-direction: column !important;
            align-items: center !important;
            text-align: center !important;
        }

        /* --- PESTAÑAS (TABS) --- */
        button[data-baseweb="tab"] p {
            font-size: 15px !important;
            font-weight: bold !important;
        }
        
        /* --- VALORES DE KPIs --- */
        [data-testid="stMetricLabel"] p { font-size: 14px !important; color: #b0b5c9 !important; }
        [data-testid="stMetricValue"] { font-size: 27px !important; }

        /* --- JERARQUÍA DEL MENÚ LATERAL (SIDEBAR) --- */
        
        /* Título Principal: "Variables del modelo" */
        [data-testid="stSidebar"] h1 {
            font-size: 27px !important; 
            color: #4eb1cb !important;
            font-weight: bold !important;
            margin-bottom: 30px !important;
        }

        /* Subtítulos de Sección: "1. Mercado", "2. Producto", "3. Impacto" */
        [data-testid="stSidebar"] h2 {
            font-size: 24px !important; 
            color: #ffffff !important;
            font-weight: bold !important;
            border-bottom: 2px solid #4eb1cb;
            padding-bottom: 8px;
            margin-top: 35px !important;
            margin-bottom: 15px !important;
        }

        /* Etiquetas de los filtros (debajo de los títulos) */
        [data-testid="stSidebar"] label p {
            font-size: 18px !important; 
            color: #e8eaf2 !important;
            font-weight: normal !important;
        }

        /* Números en Sliders, Selectores e Inputs */
        [data-testid="stSidebar"] .stSlider p, 
        [data-testid="stSidebar"] .stSelectbox div[data-baseweb="select"],
        [data-testid="stSidebar"] input {
            font-size: 15px !important;
        }
        
        /* Ajuste de los Insights */
        .insight { 
            background-color: #1c2030; border-left: 4px solid #4eb1cb; 
            border-radius: 0 8px 8px 0; padding: 14px 18px; 
            margin: 15px 0; font-size: 14px; color: #e8eaf2;
        }
    </style>
    """, unsafe_allow_html=True)
# --------------------------------------------------
# 📥 2. CARGA DE DATOS DESDE EXCEL
# --------------------------------------------------
@st.cache_data
def load_data():
    archivo_excel = "Datos_020326.xlsx"
    try:
        df_mercado = pd.read_excel(archivo_excel, sheet_name="TAM-SAM-SOM")
        df_adquisicion = pd.read_excel(archivo_excel, sheet_name="Modelo adquisición")
        return df_mercado, df_adquisicion
    except Exception as e:
        st.error(f"❌ Error leyendo el Excel. Detalle: {e}")
        st.stop()

df_mercado, df_adquisicion = load_data()

# --------------------------------------------------
# 🎛️ BARRA LATERAL (SIMULADOR DINÁMICO)
# --------------------------------------------------
st.sidebar.header("Variables del Modelo")

st.sidebar.write("")


st.sidebar.markdown("**1. Mercado**")
input_som_pct = st.sidebar.slider("Penetración Objetivo (SOM %)", min_value=1, max_value=20, value=10, step=1)

input_meta = st.sidebar.number_input("Meta de Facturación (USD)", value=20000000, step=1000000)



st.sidebar.markdown("---")

st.sidebar.markdown("**2. Producto (Adquisición)**")
input_precio = st.sidebar.number_input("Precio Justina (CAPEX USD)", value=750000, step=10000)


st.sidebar.markdown("---")

st.sidebar.markdown("**3. Impacto Clínico**")
input_ahorro = st.sidebar.slider("Ahorro x Cirugía (USD)", min_value=1000, max_value=2500, value=1929, step=10)
input_volumen = st.sidebar.slider("Volumen (Hosp. Grande)", min_value=100, max_value=500, value=300, step=10)



# --- CABECERA: TÍTULO + FILTRO EN LA MISMA LÍNEA ---
col_titulo, col_espacio, col_filtro = st.columns([5, 2, 3])

with col_titulo:
    st.title("Justina – Business Intelligence")
    
with col_filtro:
    # Título pequeño arriba del selector
    st.markdown('<p style="margin-bottom: -10px; font-size: 14px; font-weight: bold; color: #4eb1cb; padding-top: 15px;"></p>', unsafe_allow_html=True)
    
 
# --- TABS (ANCHO COMPLETO) ---
# Al estar aquí, ocupan todo el ancho y no tienen nada arriba que los bloquee
tab1, tab2, tab3 = st.tabs([
    "H1: Oportunidad de Mercado", 
    "H2: Modelos de Adquisición", 
    "H3: Impacto Clínico y ROI"
])


# ==================================================
# TAB 1 – H1: MERCADO (Con Filtros y Comparativas)
# ==================================================

# --- LÓGICA DE FILTRADO ---

with tab1:
    
    # --- FILTRO DE PAÍS SÓLO PARA ESTA PESTAÑA ---
    col_vacia, col_filtro_tab = st.columns([7, 3])
    with col_filtro_tab:
        paises = df_mercado["País"].unique()
        pais_seleccionado = st.selectbox(
            "País", 
            ["Países"] + list(paises),
            label_visibility="collapsed"
        )

    # --- LÓGICA DE FILTRADO ---
    if pais_seleccionado != "Países":
        df_filtrado = df_mercado[df_mercado["País"] == pais_seleccionado]
    else:
        df_filtrado = df_mercado
    
    # 1. Calculamos los números PRIMERO (para saber si es verde o rojo)
    tam_total = df_filtrado["Total Cirugías (TAM)"].sum()
    sam_total = df_filtrado["Mercado Direccionable (SAM)"].sum()
    som_dinamico = sam_total * (input_som_pct / 100)
    ingreso_estimado = som_dinamico * input_precio
    
    # Traemos el número de la barra lateral (los 20 millones u otro que elijan)
    meta_facturacion = input_meta 
    robots_necesarios = math.ceil(meta_facturacion / input_precio) if input_precio > 0 else 0

    # 2. DIBUJAMOS LA FILA: Título a la Izquierda (70%) | Cajita a la Derecha (30%)
    col_tit, col_rent = st.columns([7, 3])
    
    with col_tit:
        st.subheader("Cuantificación de la Oportunidad (H1)")
        
    with col_rent:
        # 1. Calculamos los robots ANTES para poder usarlos en el título de la caja
        robots_necesarios = math.ceil(meta_facturacion / input_precio) if input_precio > 0 else 0
        robots_proyectados = math.floor(ingreso_estimado / input_precio) if input_precio > 0 else 0
        
        # 2. Lógica de títulos enfocada en unidades, no en plata repetida
        if ingreso_estimado >= meta_facturacion:
            titulo_caja = f"✅ RENTABLE ( {robots_necesarios} robots )"
            texto_caja = f"El mercado nos permite ubicar **{robots_proyectados} robots** al precio actual de **${input_precio:,.0f}**. Superamos holgadamente el punto de equilibrio estructural de la empresa."
        else:
            robots_faltantes = robots_necesarios - robots_proyectados
            titulo_caja = f"⚠️ ALERTA DE ESCALA (Faltan vender {robots_faltantes} robots)"
            texto_caja = f"Para sostener la empresa necesitamos ubicar **{robots_necesarios} robots**. Hoy nuestra penetración de mercado solo nos permite vender **{robots_proyectados}**. Debemos ajustar el precio o ser más agresivos en la captura de mercado."
            
        # 3. Armamos el expander con la nueva info
        with st.expander(titulo_caja):
            st.markdown(texto_caja)
    # 3. LOS 4 KPIs DE SIEMPRE (van justo debajo del título)
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("TAM (Total Cirugías Elegibles)", f"{tam_total:,.0f}")
    col2.metric("SAM (Mercado Direccionable)", f"{sam_total:,.0f}")
    col3.metric(f"SOM ({input_som_pct}% Penetración)", f"{som_dinamico:,.0f}")
    col4.metric("Ingresos Potenciales", f"${ingreso_estimado/1_000_000:,.1f}M")
    
    st.markdown("---")
    
    
    # Gráficos de H1
    c1, c2 = st.columns(2)
    
    with c1:
        st.markdown("### Estructura del Mercado (Funnel)")
        fig_funnel = go.Figure(go.Funnel(
            y=["TAM (Total)", "SAM (Accesible)", f"SOM ({input_som_pct}%)"],
            x=[tam_total, sam_total, som_dinamico],
            
            # 🔥 ACÁ ESTÁ LA MAGIA: Obligamos a Plotly a usar nuestro formato limpio
            texttemplate="%{value:,.0f} (%{percentInitial:.1%})",
            
            # Letra blanca, en negrita y más grande para los números
            textfont=dict(size=12, color="white", family="Arial Black"), 
            
            marker={"color": ["#4eb1cb", "#f9c74f", "#f8961e"]},
            
            # Líneas conectoras en gris clarito y un poco más gruesas
            connector=dict(line=dict(color="#383838", width=2, dash="solid"))
        ))
        fig_funnel.update_layout(height=350, margin=dict(t=20, b=20, l=0, r=0))
        st.plotly_chart(fig_funnel, use_container_width=True)
        
        # 🚀 NUEVO: Caja de Insight debajo del Funnel para equilibrar el diseño
        st.markdown(f'''
            <div class="insight">
                <strong>Análisis de Penetración:</strong> El salto del mercado direccionable (SAM) a nuestra meta de captura ({input_som_pct}%) representa un escenario realista frente a competidores establecidos. El embudo demuestra que incluso con una porción menor de la demanda, el volumen justifica la inversión.
            </div>
        ''', unsafe_allow_html=True)

    with c2:
        st.markdown("### SAM por País (Dónde está la oportunidad)")
        
        # 1. EL TRUCO: Calculamos el máximo SAM de TODOS los países (sin filtrar) para fijar la escala visual
        df_mercado["SAM_limpio_global"] = pd.to_numeric(
            df_mercado["Mercado Direccionable (SAM)"], errors='coerce'
        ).fillna(0)
        max_escala_x = df_mercado["SAM_limpio_global"].max() * 1.15 # Le damos un 15% de espacio extra a la derecha

        # 2. Limpiamos los datos de la selección actual
        df_filtrado["SAM_limpio"] = pd.to_numeric(
            df_filtrado["Mercado Direccionable (SAM)"], errors='coerce'
        ).fillna(0)
        df_limpio = df_filtrado[df_filtrado["SAM_limpio"] > 0]

        # 3. Dibujamos el gráfico con la escala fija
        fig_pais = go.Figure(go.Bar(
            x=df_limpio["SAM_limpio"],
            y=df_limpio["País"].astype(str),
            orientation='h',
            marker_color="#4eb1cb",
            
            # Agregamos el numerito en la barra para más claridad
            text=df_limpio["SAM_limpio"],
            texttemplate="%{text:,.0f}",
            textposition="auto",
            textfont=dict(color="white", size=11)
        ))
        
        fig_pais.update_layout(
            template="plotly_dark", 
            height=350, 
            yaxis={'categoryorder':'total ascending'}, 
            
            # 🔥 ACÁ CLAVAMOS LA ESCALA PARA QUE NO MIENTA VISUALMENTE
            xaxis=dict(range=[0, max_escala_x]), 
            
            margin=dict(t=20, b=20, l=0, r=0)
        )
        st.plotly_chart(fig_pais, use_container_width=True)
        
        st.markdown('<div class="insight"><strong>Estrategia de Expansión (Go-to-Market):</strong> La oportunidad no está distribuida de manera pareja. La demanda direccionable (SAM) se concentra fuertemente en los países líderes del gráfico. Esto nos indica exactamente en qué mercados debemos enfocar los esfuerzos comerciales iniciales para maximizar el retorno.</div>', unsafe_allow_html=True)
        st.caption("Estimación basada en precio unitario simulado y penetración objetivo seleccionada.")
# ==================================================
# TAB 2 – H2: MODELOS DE ADQUISICIÓN (Con Costo Total Dinámico)
# ==================================================
with tab2:
    st.subheader("Reducción de Barreras de Entrada (H2)")
    

    st.markdown("---")
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### Barrera de Entrada Inicial")
        st.caption("Impacto de desembolso (Día 1) para el hospital.")

        # Estilos CSS para la tabla
        st.markdown("""
        <style>
            .tabla-barreras { width: 100%; border-collapse: collapse; margin-top: 10px; }
            .tabla-barreras th { text-align: left; padding: 10px; border-bottom: 2px solid #4eb1cb; color: #4eb1cb; font-size: 14px;}
            .tabla-barreras td { padding: 14px 10px; border-bottom: 1px solid #252a38; font-size: 15px; }
            .badge-verde { background-color: rgba(0, 245, 155, 0.15); color: #00f59b; padding: 6px 12px; border-radius: 20px; font-weight: bold; font-size: 13px; }
            .badge-rojo { background-color: rgba(230, 57, 70, 0.15); color: #e63946; padding: 6px 12px; border-radius: 20px; font-weight: bold; font-size: 13px; }
        </style>
        """, unsafe_allow_html=True)

        # Armamos la tabla HTML
        html_tabla_b = f"""
        <table class='tabla-barreras'>
            <tr>
                <th>Modelo de Negocio</th>
                <th>Inversión (Día 1)</th>
                <th>Fricción Comercial</th>
            </tr>
            <tr>
                <td><b>1. Compra Directa (CAPEX)</b></td>
                <td>${input_precio:,.0f}</td>
                <td><span class='badge-rojo'>🛑 Barrera Extrema</span></td>
            </tr>
            <tr>
                <td><b>2. Leasing Financiero</b></td>
                <td>$0</td>
                <td><span class='badge-verde'>✅ Sin Barrera</span></td>
            </tr>
            <tr>
                <td><b>3. Pago por Uso</b></td>
                <td>$0</td>
                <td><span class='badge-verde'>✅ Sin Barrera</span></td>
            </tr>
        </table>
        """
        
        st.markdown(html_tabla_b, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True) # Espacio para emparejar alturas
        st.caption("Modelos alternativos eliminan el riesgo financiero inicial, acelerando la adopción.")

    with c2:
        st.markdown("### Composición del Costo a 5 Años")
        
        # --- CÁLCULOS PARA EL GRÁFICO APILADO (100% Dinámicos) ---
        mantenimiento_anual = df_adquisicion["Costo Fijo Anual (Años 1 al 5)"].iloc[0] # 35,000
        cuota_leasing = df_adquisicion["Costo Fijo Anual (Años 1 al 5)"].iloc[1]       # 195,000
        consumible_base = df_adquisicion["Costo_ Consumibles_ Promedio_ USD"].iloc[0]  # 450
        consumible_ppu = df_adquisicion["Costo_Variable_ USD"].iloc[2]                 # 1950
        
        equipo_capex = input_precio         
        equipo_leasing = cuota_leasing * 5  
        equipo_ppu = 0                      
        
        mante_capex = mantenimiento_anual * 4  
        mante_leasing = 0                      
        mante_ppu = 0                          
        
        operativo_capex = consumible_base * input_volumen * 5
        operativo_leasing = consumible_base * input_volumen * 5
        operativo_ppu = consumible_ppu * input_volumen * 5

        # --- CREACIÓN DEL GRÁFICO APILADO (STACKED) ---
        fig_stack = go.Figure()
        
        fig_stack.add_trace(go.Bar(
            name='Equipo / Cuota', x=["Compra Directa", "Leasing", "Pago por Uso"],
            y=[equipo_capex, equipo_leasing, equipo_ppu], marker_color='#f8961e'
        ))
        fig_stack.add_trace(go.Bar(
            name='Mantenimiento', x=["Compra Directa", "Leasing", "Pago por Uso"],
            y=[mante_capex, mante_leasing, mante_ppu], marker_color='#f9c74f'
        ))
        fig_stack.add_trace(go.Bar(
            name='Consumibles / Uso', x=["Compra Directa", "Leasing", "Pago por Uso"],
            y=[operativo_capex, operativo_leasing, operativo_ppu], marker_color='#4eb1cb'
        ))

        fig_stack.update_layout(
            barmode='stack', template="plotly_dark", height=400, margin=dict(t=20, b=20, l=0, r=0),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            font=dict(size=14)
        )
        st.plotly_chart(fig_stack, use_container_width=True)

    # Insight final unificado
    st.markdown(f'''
        <div class="insight">
            <strong>Estrategia de Ventas:</strong> Mientras que la <b>Compra Directa</b> exige un desembolso masivo, el <b>Pago por Uso</b> permite al hospital pagar solo si opera. 
            A 5 años, el Pago por Uso puede parecer más costoso en total, pero es el modelo que permite una <b>adopción inmediata</b> sin trámites burocráticos de inversión.
        </div>
    ''', unsafe_allow_html=True)
# ==================================================
# TAB 3 – H3: IMPACTO CLÍNICO Y ROI (Break-Even)
# ==================================================

# DOS COLUMNAS: Izquierda (Gráfico) y Derecha (Tabla)
   
with tab3:
    st.subheader("Viabilidad Económica Hospitalaria (H3)")

    # 1. Cálculos dinámicos (Alineados correctamente hacia adentro)
    ahorro_total_anual = input_volumen * input_ahorro
    payback_anos = input_precio / ahorro_total_anual if ahorro_total_anual > 0 else 0

    # 2. KPIs Superiores (¡Los recuperamos!)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Volumen Simulado", f"{input_volumen} cx/año")
    col2.metric("Ahorro Unitario", f"${input_ahorro:,.0f}")
    col3.metric("Ahorro Total Anual", f"${ahorro_total_anual:,.0f}")
    col4.metric("Tiempo de Recupero (Payback)", f"{payback_anos:.1f} años")

    st.markdown("---")

    # 3. DOS COLUMNAS: Izquierda (Gráfico) y Derecha (Tabla)
    col_izq, col_der = st.columns(2)

    # COLUMNA IZQUIERDA: Punto de Equilibrio
    with col_izq:
        st.markdown("### Punto de Equilibrio")
        years = np.arange(0, 6) 
        cash_flow = [-input_precio] + [ahorro_total_anual] * 5
        acumulado = np.cumsum(cash_flow)

        fig_roi = go.Figure()
        fig_roi.add_trace(go.Scatter(
            x=years, y=acumulado, mode="lines+markers+text",
            line=dict(color="#4eb1cb", width=4),
            marker=dict(size=10),
            text=[f"${v/1000:.0f}k" for v in acumulado],
            textposition="top center",
            fill='tozeroy', fillcolor='rgba(78, 177, 203, 0.1)'
        ))
        fig_roi.add_hline(y=0, line_dash="dash", line_color="#f9c74f", annotation_text="BREAK-EVEN")
        fig_roi.update_layout(height=400, margin=dict(t=20, b=20, l=0, r=0), template="plotly_dark")
        st.plotly_chart(fig_roi, use_container_width=True)

    # COLUMNA DERECHA: Tabla de Viabilidad
    with col_der:
        st.markdown("### Diagnóstico de Viabilidad")
        st.caption("Análisis de requerimiento de subsidios a 5 años.")

        # Escenarios dinámicos
        escenarios = {"Grande": 1.2, "Mediano": 0.6, "Chico": 0.2}
        
        # Estilos visuales
        st.markdown("""
        <style>
            .tabla-estado { width: 100%; border-collapse: collapse; margin-top: 10px; }
            .tabla-estado th { text-align: left; padding: 10px; border-bottom: 2px solid #4eb1cb; color: #4eb1cb; font-size: 14px;}
            .tabla-estado td { padding: 14px 10px; border-bottom: 1px solid #252a38; font-size: 15px; }
            .badge-verde { background-color: rgba(0, 245, 155, 0.15); color: #00f59b; padding: 6px 12px; border-radius: 20px; font-weight: bold; font-size: 13px; }
            .badge-amarillo { background-color: rgba(249, 199, 79, 0.15); color: #f9c74f; padding: 6px 12px; border-radius: 20px; font-weight: bold; font-size: 13px; }
            .badge-rojo { background-color: rgba(230, 57, 70, 0.15); color: #e63946; padding: 6px 12px; border-radius: 20px; font-weight: bold; font-size: 13px; }
        </style>
        """, unsafe_allow_html=True)

        html_tabla = "<table class='tabla-estado'><tr><th>Escenario (Volumen)</th><th>Estado Financiero</th></tr>"

        for n, factor in escenarios.items():
            vol_esc = input_volumen * factor
            ahorro_5a = vol_esc * input_ahorro * 5
            faltante = input_precio - ahorro_5a
            pct = (faltante / input_precio) * 100 if faltante > 0 else 0
            
            if pct == 0:
                estado = "<span class='badge-verde'>✅ Autosustentable</span>"
            elif pct < 50:
                estado = f"<span class='badge-amarillo'>⚠️ Subsidio del {pct:.0f}%</span>"
            else:
                estado = f"<span class='badge-rojo'>🛑 Subsidio del {pct:.0f}%</span>"
                
            html_tabla += f"<tr><td><b>Hospital {n}</b></td><td>{estado}</td></tr>"
            
        html_tabla += "</table>"
        st.markdown(html_tabla, unsafe_allow_html=True)

    # 4. Insight unificado abajo
    st.markdown(f'''
        <div class="insight">
            <strong>Análisis Estratégico:</strong> Mientras el modelo es autosustentable en centros de alto volumen, 
            la tabla de diagnóstico identifica la brecha financiera en hospitales menores. 
            Esta visibilidad permite planificar donaciones estratégicas o financiamiento público dirigido.
        </div>
    ''', unsafe_allow_html=True)