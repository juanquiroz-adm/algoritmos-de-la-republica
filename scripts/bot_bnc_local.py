import pdfplumber
import re
import os
from collections import Counter

# 1. CONFIGURACIÓN DEL ENTORNO LOCAL
directorio_actual = os.getcwd()
archivos_bnc = [archivo for archivo in os.listdir(directorio_actual) if archivo.endswith('.pdf')]

# Stopwords ajustadas al español antiguo que vimos en tus PDFs
stopwords = ['de', 'la', 'el', 'en', 'y', 'a', 'los', 'que', 'por', 'las', 'con', 'un', 'para', 'una', 'su', 'se', 'del', 'al', 'es', 'como', 'o', 'sus', 'no', 'lo', 'mas', 'fue', 'este', 'esta']

corpus_maestro = ""

print("=== INICIANDO PROCESAMIENTO MASIVO BNC ===")
print(f"Archivos detectados en el directorio: {len(archivos_bnc)}\n")

try:
    # 2. BUCLE DE EXTRACCIÓN
    for indice, archivo in enumerate(archivos_bnc, start=1):
        print(f"⏳ [Procesando {indice}/{len(archivos_bnc)}] Leyendo: {archivo} ...")
        
        try:
            with pdfplumber.open(archivo) as pdf:
                # Leeremos todas las páginas de los documentos
                for pagina in pdf.pages:
                    texto = pagina.extract_text()
                    if texto:
                        corpus_maestro += texto + " "
            print(f"   ✅ Texto extraído de {archivo}")
        except Exception as e:
            print(f"   ❌ Error al leer {archivo}: {e}")

    # 3. TRANSFORMACIÓN Y LIMPIEZA
    print("\n🧠 [PROCESANDO BIG DATA HISTÓRICO] Limpiando el corpus unificado...")
    texto_limpio = corpus_maestro.lower()
    
    # Limpieza estricta: solo letras, ideal para el OCR antiguo
    texto_limpio = re.sub(r'[^a-záéíóúñ]+', ' ', texto_limpio)
    
    palabras = texto_limpio.split()
    palabras_utiles = [p for p in palabras if p not in stopwords and len(p) > 3]
    
    print(f"✅ Limpieza completada. Total de palabras analizadas: {len(palabras_utiles)}")

    # 4. ANÁLISIS DE DATOS
    print("\n📊 RESULTADOS: TOP 10 PALABRAS EN LA PRENSA DEL SIGLO XIX (BNC):")
    contador = Counter(palabras_utiles)
    top_10 = contador.most_common(10)

    for palabra, frecuencia in top_10:
        print(f" -> {palabra.upper()}: {frecuencia} veces")

    print("\n✅ CICLO BATCH SUPERADO CON DATOS REALES DE LA BNC.")

except Exception as e:
    print(f"\n❌ ERROR CRÍTICO: {e}")