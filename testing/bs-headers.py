import requests

# URL de la página web
url = 'https://www.tiffany.es/accessories/shop/eyewear/'

# Definir encabezados personalizados
headers = {
   "authority": "www.tiffany.es",
   "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
   "accept-language":"es-ES,es;q=0.9,en;q=0.8,ca;q=0.7",
   "cache-control": "max-age=0",
  
   "upgrade-insecure-requests": "1",
   "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
}

# Realizar la solicitud con encabezados personalizados
response = requests.get(url, headers=headers)

# Imprimir el contenido de la página
print(response.text)

