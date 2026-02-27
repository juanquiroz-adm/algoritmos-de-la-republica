import requests
from bs4 import BeautifulSoup

# URL del catálogo de la BNC filtrada por "Prensa Colombiana"
url_catalogo = "https://catalogoenlinea.bibliotecanacional.gov.co/client/es_ES/bd/?rm=PRENSA+COLOMBI0%7C%7C%7C1%7C%7C%7C4%7C%7C%7Ctrue"

# Simulamos ser un navegador Firefox desde Ubuntu para evitar bloqueos (Anti-Scraping)
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"
}

print("--- INICIANDO PROTOCOLO DE CONEXIÓN BNC ---")
print(f"Target: {url_catalogo}\n")

try:
    # Lanzamos la petición GET con un timeout de seguridad
    respuesta = requests.get(url_catalogo, headers=headers, timeout=15)
    
    # Verificamos si el servidor nos dio luz verde
    if respuesta.status_code == 200:
        print("✅ ESTADO: CONEXIÓN EXITOSA (Código HTTP 200)")
        
        # Parseamos el HTML (El DOM de la página)
        sopa = BeautifulSoup(respuesta.text, 'html.parser')
        
        # Extraemos el título de la página para confirmar que estamos en el lugar correcto
        titulo = sopa.find('title').text if sopa.find('title') else 'Sin título'
        print(f"📄 Título interceptado: {titulo.strip()}")
        
        # Contamos cuántos enlaces detecta el bot en la página
        enlaces = sopa.find_all('a')
        print(f"🔗 El radar detectó {len(enlaces)} hipervínculos en el DOM de esta página.")
        
        print("\n✅ DIAGNÓSTICO: PRUEBA DE CONCEPTO (PoC) SUPERADA.")
        print("El servidor no bloquea nuestro script. La automatización del proyecto es 100% viable.")
        
    else:
        print(f"❌ ALERTA: El servidor nos detectó o falló. Código: {respuesta.status_code}")

except Exception as e:
    print(f"❌ ERROR CRÍTICO DE RED: {e}")
