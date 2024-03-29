import requests
from bs4 import BeautifulSoup

def get_google():
    # Desactivar las advertencias de solicitud no segura (por ejemplo, ignorar los errores de certificado SSL)
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    
    url = "https://novoatacarejo.com/oferta/xt/xt.listar.php"
    headers = {
         'Accept': "application/json, text/javascript, */*; q=0.01",
         "Accept-Language": "es-ES,es;q=0.9,en;q=0.8,ca;q=0.7",
         'Connection': "keep-alive",
         "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
         'Origin': 'https://novoatacarejo.com',
         'Referer': 'https://novoatacarejo.com/oferta/mobile.php',
         "User-Agent":
           "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
         "X-Requested-With": "XMLHttpRequest",
       }
    body = 'id=19'
    try:
        response = requests.post(url, headers=headers, data=body, verify=False)
        response.raise_for_status()
        # Manejar la respuesta como JSON
        data = response.json()
        print(data)  # Puedes manejar los datos de la respuesta JSON aquí
    except requests.exceptions.RequestException as e:
        print(f"Ocurrió un error durante la solicitud HTTP: {e}")

if __name__ == "__main__":
    search_results = get_google()
