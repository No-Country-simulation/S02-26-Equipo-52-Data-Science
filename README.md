# 🤖 Justina – Business Intelligence para Robótica Quirúrgica
## Framework Analítico de Adopción Global y Viabilidad Económica

---

### 🌐 Accesos y Recursos del Proyecto

Antes de profundizar en la documentación técnica, puede acceder a las herramientas interactivas del proyecto a través de los siguientes enlaces:

* **🖥️ Dashboard Interactivo (Streamlit):** [Link al Dashboard aquí]
* **💻 Repositorio de Código (GitHub):** [Link al Repositorio aquí]
    * *Nota: Incluye el motor de proyecciones paramétricas desarrollado en Google Colab y el script de visualización de la aplicación.*

---

### 📌 Descripción General
**Justina** es una plataforma de Business Intelligence (BI) diseñada para transformar datos complejos de la industria MedTech en decisiones estratégicas. El proyecto evalúa la factibilidad económica y operativa de introducir sistemas robóticos asistidos para cirugía renal en un mercado global altamente competitivo.

A través de un modelo de datos integrado, Justina permite simular escenarios de mercado, comparar estructuras de adquisición (CAPEX/OPEX) y proyectar el retorno de inversión (ROI) hospitalario basado en eficiencia clínica real.

---

### 🎯 Objetivos del Proyecto
* **📊 Dimensionamiento Global:** Cuantificación del mercado (TAM, SAM, SOM) utilizando datos oncológicos de la OMS (GLOBOCAN 2022/2025).
* **💰 Optimización Financiera:** Evaluación de modelos de Pago por Uso para reducir barreras de entrada.
* **🏥 Simulación de ROI:** Proyección de flujo de caja y payback hospitalario basado en ahorros operativos validados.
* **🧠 Soporte de Decisión:** Herramienta interactiva para instituciones de salud y fabricantes de tecnología médica.

---

### 🏗️ Arquitectura del Proyecto y Enfoque Multidisciplinario
El éxito del modelo reside en la integración de tres disciplinas clave:

1.  **Data Architecture:** ETL y estructuración de bases de datos para normalizar registros globales de incidencia oncológica.
2.  **Data Science (Pilar de Modelado):** Desarrollo en entorno **Python (Google Colab)** de un modelo dinámico para proyectar métricas a X años. Utilizando a **América Latina (SAM LatAm ~USD 400M)** como caso de estudio base, se aplicaron tasas CAGR (12-15%) y pruebas de sensibilidad (±40%) para validar la robustez matemática del negocio.
3.  **Business Intelligence:** Diseño de un dashboard interactivo en **Streamlit** que escala el modelo regional a una visión global, permitiendo simulaciones específicas por país.

---

### 🧠 Hipótesis Estratégicas Validadas
* **H1 (Mercado):** Existe una demanda cuantificable en centros con capacidad laparoscópica previa que aún no han dado el salto a la robótica.
* **H2 (Adopción):** La migración de CAPEX a modelos de Leasing Operativo (OPEX) o Pago por Uso acelera la penetración de mercado al eliminar el desembolso inicial.
* **H3 (Impacto):** La reducción de complicaciones clínicas genera un ahorro operativo (~$1.220 - $1.929 USD por cirugía) que contribuye al autofinanciamiento del sistema.

---

### 🔬 Estructura del Dashboard (Pestañas)

#### 1. Oportunidad de Mercado (TAM-SAM-SOM)
Análisis detallado de incidencia por país y segmentación de centros hospitalarios elegibles. 
* **Visualización:** Gráfico de Funnel y comparativa por país.
* **KPIs:** Volumen Quirúrgico, Escenarios de Ingresos y Diagnóstico de Escala.

#### 2. Modelos de Adquisición
Comparativa de la barrera de entrada entre Compra Directa, Leasing y Pago por Uso.
* **Insight Clave:** Identificación de la reducción de fricción comercial mediante modelos basados en el uso, alineados con tendencias actuales de líderes como Intuitive Surgical.

#### 3. Viabilidad Económica y ROI Hospitalario
Simulador de rentabilidad paramétrico para el centro de salud.
* **Gráfico de Punto de Equilibrio:** Proyección temporal del Payback.
* **Diagnóstico de Viabilidad:** Identificación automática de necesidad de subsidios en hospitales de bajo volumen.

---

### 📚 Fundamentación Científica (Fuentes)
El modelo se sustenta en evidencia de vanguardia (2025-2026):
* **Mercado:** Global Cancer Observatory (GLOBOCAN 2022/2025).
* **Costo-Efectividad:** Tang Y, & Dou B. (Agosto, 2025) - *Frontiers in Public Health*.
* **Guías Clínicas:** EAU Guidelines on Renal Cell Carcinoma (2025 Update).
* **Tendencias:** Rojas Burbano J, et al. (Abril, 2025) - *Cureus Journal of Medical Science*.

---

### 🛠 Tecnologías y Herramientas
* **Lenguajes:** Python (Pandas, NumPy, Plotly).
* **Entornos:** Google Colab / Jupyter Notebooks.
* **Despliegue:** Streamlit Cloud.
* **Colaboración:** GitHub (Control de versiones).

👥 Equipo (S02-26-Equipo 52)
*Antonio Pérez Sandoval – Data Scientist
*Franco Gastón Cuello – Data Architect
*Marianela Pi – BI Analyst
*Lourdes Gabriela Sánchez Almaraz – Data Scientist

*⚠️ Estado del Proyecto
*🟢 Finalizado / Productivo

El simulador permite parametrización dinámica y está listo para ser utilizado en presentaciones de inversión y planificación estratégica de salud.

