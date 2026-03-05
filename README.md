# S02-26-Equipo-52-Data-Science
Business Intelligence para robótica quirúrgica: modelo de adopción y escalabilidad.
# 🤖 Justina – Business Intelligence para Robótica Quirúrgica: Modelo de Adopción y Escalabilidad

## 📌 Descripción General

**Justina** es una iniciativa académico-tecnológica en plataforma de Business Intelligence (BI) que evalúa la factibilidad económica y operativa de desarrollar un sistema robótico asistido para **cirugía renal mínimamente invasiva** diseñada para transformar datos complejos de la industria MedTech en decisiones estratégicas. 

 
> A través de un modelo de datos integrado, Justina permite  
> **simular escenarios de mercado, comparar estructuras de adquisición (CAPEX/OPEX) y proyectar el retorno de inversión (ROI)** hospitalario basado en eficiencia clínica real.

Este repositorio contiene el framework de **Business Intelligence** aplicado a healthtech, incluyendo análisis de mercado, benchmarks competitivos, modelado económico, simulación de escenarios y dashboards interactivos.

---

## 🎯 Objetivos del Proyecto

- 📊 Dimensionamiento Global: Cuantificación del mercado (**TAM, SAM, SOM**) utilizando datos oncológicos de la OMS (GLOBOCAN 2022).  
- 💰 Comparar costos y modelos de negocio de plataformas existentes (da Vinci, Versius, Hugo RAS).  
- 🏥 Diseñar un modelo económico preliminar para **Justina** (CAPEX, OPEX, TCO).  
- 🔍 Simulación de ROI: Proyección de flujo de caja y payback hospitalario basado en ahorros operativos validados.  
- 📈 Definir **KPIs** de impacto clínico y económico.  
- 🧠 Construir herramientas interactivas (dashboards) para simulación de escenarios y toma de decisiones.

---

## 🏥 Contexto de la Industria

El mercado global de robótica quirúrgica está dominado por:

- **da Vinci** (Intuitive Surgical) – líder con modelo razor-blade  
- **Versius** (CMR Surgical) – modular y más flexible  
- **Hugo RAS** (Medtronic) – enfoque en integración y penetración competitiva  

En América Latina la adopción es limitada por:

- Altos costos de entrada (CAPEX)  
- Modelos de negocio poco adaptados  
- Heterogeneidad en sistemas de salud  
- Volúmenes quirúrgicos variables por país  

Esto representa una oportunidad para soluciones optimizadas regionalmente, con menor CAPEX, financiamiento flexible y enfoque en cirugía especializada (renal).

---

🏗️ Arquitectura del Proyecto y Enfoque Multidisciplinario

El éxito del modelo reside en la integración de tres disciplinas clave:

Data Architecture: ETL y estructuración de bases de datos para normalizar registros globales.

Data Science: Modelado predictivo y análisis de escenarios para proyectar curvas de adopción y eficiencia.

Business Intelligence: Diseño de un dashboard interactivo en Streamlit que traduce métricas técnicas en insights de negocio.

## 🧠 Hipótesis Estratégicas

1. **H1 – Oportunidad cuantificable**  
   Mercado: Existe una demanda cuantificable en centros con capacidad laparoscópica previa que aún no han dado el salto a la robótica.

2. **H2 – Reducción de barreras**  
   La migración de CAPEX a Modelos flexibles (Leasing Operativo, pago por uso) amplían el universo de hospitales adoptantes.

3. **H3 – Impacto Clínico**  
   La reducción de complicaciones clínicas genera un ahorro operativo que autofinancia el costo del sistema.

---

## 🔬 Estructura del Dashboard (Pestañas)

1. Oportunidad de Mercado (TAM-SAM-SOM)
Análisis detallado de incidencia por país y segmentación de centros hospitalarios elegibles.

KPIs: Volumen Quirúrgico, Escenarios de Ingresos y Penetración por Región.

2. Modelos de Adquisición
Comparativa de la barrera de entrada entre Compra Directa, Leasing y Pago por Uso.

Insight Clave: Basado en la tendencia de Intuitive Surgical (da Vinci) hacia el usage-based operating lease.

3. Viabilidad Económica y ROI Hospitalario
Simulador de rentabilidad para el centro de salud.

Ahorro Unitario: $1.929 USD por procedimiento (Validado por evidencia científica).

KPIs: Tiempo de Recupero (Payback) y Punto de Equilibrio (Break-even).

### 1️⃣ Análisis de Mercado (TAM, SAM, SOM)

**TAM (Total Addressable Market)**  
Total de procedimientos renales potencialmente elegibles para asistencia robótica en LATAM.

**SAM (Serviceable Available Market)**  
Procedimientos realizados en hospitales que cuentan con:
- Infraestructura quirúrgica adecuada  
- Capacidad laparoscópica  
- Potencial de inversión en tecnología  

**SOM (Serviceable Obtainable Market)**  
Porción realista del mercado que podría capturarse considerando:
- Curvas de adopción  
- Competencia existente  
- Estrategia de precios  

---

### 2️⃣ Benchmark Competitivo de Costos

| Plataforma | Modelo de Negocio               | CAPEX      | OPEX            | Lógica de Ingresos     |
|------------|---------------------------------|------------|-----------------|------------------------|
| da Vinci   | Venta de sistema + instrumentos | Alto       | Alto recurrente | Razor-razorblade       |
| Versius    | Modular / Flexible              | Medio-Alto | Recurrente      | Orientado a servicio   |
| Hugo RAS   | Entrada competitiva             | Medio      | Recurrente      | Penetración de mercado |

Variables clave analizadas:

- Precio del sistema
- Vida útil de instrumentos
- Costo por procedimiento
- Contratos de mantenimiento
- Crecimiento de base instalada
- Distribución de ingresos (Sistemas vs Instrumentos y Accesorios vs Servicios)

---

### 3️⃣ Descomposición del Modelo de Ingresos

Se analizan dos grandes fuentes:

**Ingresos CAPEX**
- Venta de sistemas

**Ingresos OPEX**
- Instrumentos y accesorios
- Contratos de mantenimiento
- Servicios y soporte técnico

Normalización clave:

Ingreso por Procedimiento = Ingresos OPEX Totales / Número Total de Procedimientos Robóticos

Esto permite comparar empresas y regiones bajo una misma métrica operativa.

---

## 📈 Métricas Clave Analizadas

- Base instalada por país
- Procedimientos por sistema por año
- Ingreso por sistema
- Ingreso por procedimiento
- Ratio de ingresos por instrumentos
- % de penetración de mercado
- Periodo de recuperación (visión hospital)
- TIR (visión inversionista)

---

## 🔬 Metodología

1. Análisis de reportes financieros públicos
2. Bases de datos de sistemas de salud
3. Estimación de volúmenes quirúrgicos
4. Filtrado de elegibilidad (cirugía renal)
5. Modelamiento económico en Python y Excel
6. Simulación de escenarios

---

## 📚 Fundamentación Científica (Fuentes)

El modelo se sustenta en evidencia de vanguardia (2025-2026):

Mercado: Global Cancer Observatory (GLOBOCAN 2022/2025).

Costo-Efectividad: Tang Y, & Dou B. (Agosto, 2025) - Frontiers in Public Health.

Guías Clínicas: EAU Guidelines on Renal Cell Carcinoma (2025 Update).

Tendencias: Rojas Burbano J, et al. (Abril, 2025) - Cureus Journal of Medical Science.

---

## 👥 Equipo (S02-26-Equipo 52)

Equipo interdisciplinario con perfiles en Business Intelligence, ingeniería biomédica, economía de la salud y ciencia de datos.

- **Marianela Pi**  – Data Scientist
- **Franco Gastón Cuello** – Data Architect
- **Antonio Pérez Sandoval** – BI Analyst
- **Lourdes Gabriela Sanchez Almaraz** – Data Scientist

---

## 🛠 Tecnologías y Herramientas

- Lenguajes: Python (Pandas, NumPy, Matplotlib, Plotly)  
- Despliegue: Streamlit / Jupyter Notebooks  
- Modelado: Excel & Python para proyecciones financieras  
- GitHub para control de versiones  
- Colaboración: GitHub & Google Drive para gestión de Datasets  

---

## 📌 Estado Actual (marzo 2026)

- 🟢 Framework competitivo y análisis de mercado completado  
- 🟢 Modelos determinísticos implementados  
- 🟢 Dashboard interactivo en desarrollo / refinamiento  

El simulador permite parametrización dinámica y está listo para ser utilizado en presentaciones de inversión y planificación estratégica de salud.

## 📬 Contacto y Colaboraciones

Para preguntas, datasets, contribuciones o posibles alianzas:  
Abre un issue en este repositorio o contacta directamente al equipo.

¡Gracias por tu interés en **Justina** – construyendo robótica quirúrgica accesible para América Latina!
