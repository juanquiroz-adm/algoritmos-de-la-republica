# 🏛️ Algoritmos de la República: Suite de Auditoría Hemerográfica

**Un ecosistema de herramientas en Python para la extracción, limpieza y análisis de la prensa colombiana del siglo XIX (BNC).**

## 🚀 Componentes del Sistema

El proyecto se divide en 4 módulos tácticos que cubren todo el ciclo de vida de los datos:

1.  **Módulo de Reconocimiento (`explorador_bnc.py`)**: Web Scraping avanzado con `BeautifulSoup` para interceptar el catálogo digital de la Biblioteca Nacional y evadir bloqueos de Anti-Scraping.
2.  **Motor de Extracción Masiva (`bot_masivo.py`)**: Procesamiento por lotes (Batch Processing) que descarga documentos desde servidores remotos (OEA/BNC) y extrae contenido en tiempo real.
3.  **Procesador Local (`bot_bnc_local.py`)**: Script optimizado para la lectura masiva de archivos PDF locales, unificando el corpus maestro para análisis de Big Data.
4.  **Minero de Texto NLP (`minero_nlp.py`)**: El cerebro del análisis. Limpieza profunda mediante Regex, filtrado de *stopwords* históricas y generación de estadísticas de frecuencia léxica.

## 🛠️ Stack Tecnológico
* **Extracción:** `requests`, `BeautifulSoup4`
* **Procesamiento PDF:** `pdfplumber`
* **Análisis:** `collections.Counter`, `Regular Expressions (re)`

## 📊 Caso de Estudio Actual
Análisis del ejemplar **"El Siglo" (Febrero, 1893)**. El sistema permite identificar los tópicos dominantes de la retórica conservadora/liberal de la época mediante la cuantificación de términos clave.

---
**Juan Quiroz** | *Analista Político y Desarrollador* [🌐 Ver Laboratorio de Datos](https://www.naujzoriuq.site/laboratorio)