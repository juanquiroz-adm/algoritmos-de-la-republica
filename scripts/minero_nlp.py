import pdfplumber
import re
from collections import Counter

# Nombre del archivo que ya tienes descargado
archivo = "ps19_elsiglo_febrero_1893.pdf"

# Lista de palabras inútiles que no queremos contar (Stopwords básicas)
stopwords = ['de', 'la', 'el', 'en', 'y', 'a', 'los', 'que', 'por', 'las', 'con', 'un', 'para', 'una', 'su', 'se', 'del', 'al', 'es', 'como', 'o']

print(f"--- INICIANDO EXTRACCIÓN Y MINERÍA DE TEXTO ---")
print(f"Procesando: {archivo}...\n")

texto_completo = ""

try:
    # 1. EXTRACCIÓN
    with pdfplumber.open(archivo) as pdf:
        # Leemos todas las páginas del PDF
        for i, pagina in enumerate(pdf.pages):
            texto_extraido = pagina.extract_text()
            if texto_extraido:
                texto_completo += texto_extraido + " "
                
    print(f"✅ Extracción completada. Caracteres totales leídos: {len(texto_completo)}")

    # 2. LIMPIEZA DE DATOS (Transformación)
    # Convertimos todo a minúsculas
    texto_limpio = texto_completo.lower()
    # Quitamos signos de puntuación y números usando Regex (dejamos solo letras)
    texto_limpio = re.sub(r'[^a-záéíóúñ]+', ' ', texto_limpio)
    
    # Separamos en palabras
    palabras = texto_limpio.split()
    
    # Filtramos las stopwords y palabras muy cortas
    palabras_utiles = [palabra for palabra in palabras if palabra not in stopwords and len(palabra) > 3]

    print(f"✅ Limpieza completada. Palabras útiles a analizar: {len(palabras_utiles)}\n")

    # 3. ANÁLISIS (Frecuencia)
    # Contamos las palabras más comunes
    contador = Counter(palabras_utiles)
    top_10 = contador.most_common(10)

    print("📊 TOP 10 PALABRAS MÁS FRECUENTES EN EL DOCUMENTO:")
    for palabra, frecuencia in top_10:
        print(f" - {palabra.upper()}: {frecuencia} veces")

    print("\n✅ CICLO COMPLETO DE MINERÍA SUPERADO.")

except Exception as e:
    print(f"❌ Error en el procesamiento: {e}")