import requests
import pdfplumber
import re
import os
import time
from collections import Counter

# 1. CONFIGURACIÓN DEL CORPUS MÚLTIPLE
# Usamos 3 documentos políticos/legales colombianos reales alojados en servidores estables (OEA)
# En tu proyecto, esta lista se llenará sola con la Araña.
urls_objetivos = [
    "https://www.oas.org/juridico/spanish/mesicic2_col_ley_190_1995.pdf", # Doc 1: Estatuto Anticorrupción
    "https://www.oas.org/juridico/spanish/mesicic2_col_ley_489_1998.pdf", # Doc 2: Ley de Administración
    "https://www.oas.org/juridico/spanish/mesicic2_col_constitucion.pdf"  # Doc 3: Constitución de Colombia
]

archivo_temporal = "documento_en_transito.pdf"
stopwords = ['de', 'la', 'el', 'en', 'y', 'a', 'los', 'que', 'por', 'las', 'con', 'un', 'para', 'una', 'su', 'se', 'del', 'al', 'es', 'como', 'o', 'sus', 'no', 'lo', 'o', 'las', 'como', 'más']

# Aquí guardaremos el texto de TODOS los documentos combinados
corpus_maestro = ""

print("=== INICIANDO EXTRACCIÓN MASIVA (BATCH PROCESSING) ===")
print(f"Total de documentos en la cola: {len(urls_objetivos)}\n")

# Simulamos ser un navegador real
headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"}

try:
    # 2. EL BUCLE DE AUTOMATIZACIÓN (El corazón del bot)
    for indice, url in enumerate(urls_objetivos, start=1):
        print(f"⏳ [Descargando {indice}/{len(urls_objetivos)}] Conectando a servidor...")
        
        # Descarga
        respuesta = requests.get(url, headers=headers, timeout=30)
        if respuesta.status_code == 200:
            with open(archivo_temporal, 'wb') as f:
                f.write(respuesta.content)
            print(f"   ✅ Descarga OK. Extrayendo texto (esto puede tomar unos segundos)...")
            
            # Extracción
            with pdfplumber.open(archivo_temporal) as pdf:
                # Para la prueba, leeremos solo las primeras 5 páginas de cada PDF 
                # (La Constitución tiene 140 páginas, queremos que el script termine hoy)
                paginas_a_leer = pdf.pages[:5] 
                
                for pagina in paginas_a_leer:
                    texto = pagina.extract_text()
                    if texto:
                        corpus_maestro += texto + " "
            
            # Limpieza del disco
            if os.path.exists(archivo_temporal):
                os.remove(archivo_temporal)
            print(f"   ✅ Texto extraído y archivo temporal destruido.")
            
            # Pausa de 2 segundos para no saturar el servidor (Cortesía de Scraping)
            time.sleep(2)
        else:
            print(f"   ❌ Error HTTP {respuesta.status_code} en Doc {indice}")

    # 3. PROCESAMIENTO NLP DEL CORPUS MAESTRO
    print("\n🧠 [PROCESANDO BIG DATA] Limpiando el corpus unificado...")
    texto_limpio = corpus_maestro.lower()
    # Dejamos solo letras, quitamos números y símbolos
    texto_limpio = re.sub(r'[^a-záéíóúñ]+', ' ', texto_limpio)
    
    palabras = texto_limpio.split()
    # Filtramos palabras inútiles y muy cortas
    palabras_utiles = [p for p in palabras if p not in stopwords and len(p) > 3]
    
    print(f"✅ Limpieza completada. Total de palabras clave extraídas de los 3 documentos: {len(palabras_utiles)}")

    # 4. ANÁLISIS ESTADÍSTICO
    print("\n📊 RESULTADOS: TOP 10 PALABRAS MÁS FRECUENTES EN TODO EL CORPUS:")
    contador = Counter(palabras_utiles)
    top_10 = contador.most_common(10)

    for palabra, frecuencia in top_10:
        print(f" -> {palabra.upper()}: {frecuencia} veces")

    print("\n✅ EJECUCIÓN DEL BUCLE 100% COMPLETADA. EL SISTEMA ES OPERATIVO.")

except Exception as e:
    print(f"\n❌ ERROR CRÍTICO DURANTE LA EJECUCIÓN: {e}")