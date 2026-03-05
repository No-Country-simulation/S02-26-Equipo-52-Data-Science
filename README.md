# S02-26-Equipo-52-Data-Science
Business Intelligence para robótica quirúrgica: modelo de adopción y escalabilidad.
# 🤖 Justina – Business Intelligence para Robótica Quirúrgica: Modelo de Adopción y Escalabilidad

## 📌 Descripción General

**Justina** es una iniciativa académico-tecnológica que evalúa la factibilidad de desarrollar un sistema robótico asistido para **cirugía renal mínimamente invasiva**.

El proyecto aborda el principal desafío en esta etapa temprana: no solo tecnológico, sino **estratégico y económico**.

> Pregunta central:  
> **¿Existe un modelo de adopción y negocio viable para robótica quirúrgica en América Latina?**

Este repositorio contiene el framework de **Business Intelligence** aplicado a healthtech, incluyendo análisis de mercado, benchmarks competitivos, modelado económico, simulación de escenarios y dashboards interactivos.

---

## 🎯 Objetivos del Proyecto

- 📊 Dimensionar el mercado potencial (**TAM, SAM, SOM**) con foco regional.  
- 💰 Comparar costos y modelos de negocio de plataformas existentes (da Vinci, Versius, Hugo RAS).  
- 🏥 Diseñar un modelo económico preliminar para **Justina** (CAPEX, OPEX, TCO).  
- 🔍 Explorar estrategias de adopción en hospitales públicos, privados y universitarios.  
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

## 🧠 Hipótesis Estratégicas

1. **H1 – Oportunidad cuantificable**  
   Existe potencial de expansión en países seleccionados, con diferencias en penetración y capacidad de inversión.

2. **H2 – Reducción de barreras**  
   Modelos flexibles (leasing, pago por uso) amplían el universo de hospitales adoptantes.

3. **H3 – Justificación económica**  
   El impacto clínico (menos días de internación, menos complicaciones) genera ahorros que justifican la inversión hospitalaria.

---

## 🏗️ Estructura del Modelo

Lógica secuencial:  
**Mercado → Impacto Clínico → ROI Hospitalario → Modelo Financiero → Sostenibilidad Empresarial**

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

### 4️⃣ Modelado de Adopción en LATAM

Simulación basada en:

**Segmentación hospitalaria**
- Tier 1: Clínicas privadas de alta complejidad
- Tier 2: Centros regionales de referencia
- Hospitales públicos

**Factores de adopción**
- Volumen de procedimientos
- Modelos de financiamiento
- Prestigio clínico
- Estructura de reembolso

**Escenarios**
- Conservador
- Moderado
- Agresivo

---


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

## 🧮 Preguntas Analíticas Clave

- ¿Cuál es el volumen mínimo de procedimientos para alcanzar breakeven en Chile?
- ¿Qué tan sensible es la adopción al precio de los instrumentos?
- ¿Un modelo de menor CAPEX aceleraría la captura del SOM?
- ¿Qué porcentaje de cirugías renales en LATAM son económicamente robotizables?

---

## 💻 Dashboard Interactivo

Se desarrolló una aplicación para simular escenarios en tiempo real.


**Características principales:**

- Sliders para ajustar CAGR, adopción, CAPEX, OPEX, etc.  
- Gráficos interactivos TAM/SAM/SOM  
- Proyecciones financieras (ingresos, cash-flow, ROI, break-even)  
- Exportación a CSV de resultados

---

## 👥 Equipo

Equipo interdisciplinario con perfiles en Business Intelligence, ingeniería biomédica, economía de la salud y ciencia de datos.

- **Marianela Pi** 
- **Franco Gastón Cuello**  
- **Antonio Pérez Sandoval** 
- **Lourdes Gabriela Sanchez Almaraz**

---

## 🛠 Tecnologías y Herramientas

- Python (Pandas, NumPy, Matplotlib, Plotly)  
- Streamlit / Jupyter Notebooks  
- Modelamiento financiero en Excel  
- GitHub para control de versiones  
- Google Drive para datasets y materiales colaborativos:  
  [Carpeta del proyecto](https://drive.google.com/drive/folders/1UMhbTtkFWXMtt9gV0WXYhT_VbQWczDfO)

---

## 📌 Estado Actual (marzo 2026)

- 🟢 Framework competitivo y análisis de mercado completado  
- 🟢 Modelos determinísticos y Monte Carlo implementados  
- 🟡 Simulación de adopción hospitalaria en progreso  
- 🟡 Dashboard interactivo en desarrollo / refinamiento  
- 🟡 Preparación para validación con datos reales y stakeholders

---

## ⚠ Limitaciones

- Análisis basado en datos públicos, benchmarks y supuestos explícitos  
- Sensible a variaciones en volumen quirúrgico, ahorro clínico y adopción  
- Aún sin validación empírica directa en hospitales  
- Proyecto académico de factibilidad – no representa un dispositivo comercial

---

## 🚀 Próximos Pasos

- Refinar curvas de adopción por país y tier hospitalario  
- Incorporar NPV y análisis de sensibilidad avanzado  
- Desplegar dashboard público (Streamlit Sharing / Hugging Face)  
- Buscar alianzas para validación clínica/económica  
- Preparar pitch para financiamiento / aceleradoras healthtech

---

## 📬 Contacto y Colaboraciones

Para preguntas, datasets, contribuciones o posibles alianzas:  
Abre un issue en este repositorio o contacta directamente al equipo.

¡Gracias por tu interés en **Justina** – construyendo robótica quirúrgica accesible para América Latina! 🇦🇷🇲🇽🇧🇷
