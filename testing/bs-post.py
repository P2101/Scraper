from bs4 import BeautifulSoup
import requests
import json

headers = {
    'authority': 'www.tiffany.es',
    'accept': 'application/json',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8,ca;q=0.7',
    'content-type': 'application/json',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'x-ibm-client-id': 'b9a8bfef128b495f8f17fb3cdeba5555',
    'x-ibm-client-secret': '73805214423d4AaebC96aD5581dbcf0b',
}

# Configura el cuerpo de la solicitud como un diccionario directamente
body = {
    "assortmentID": 2401,
    "sortTypeID": 5,
    "categoryid": 476276,
    "navigationFilters": [241476276, 2401],
    "recordsOffsetNumber": 0,
    "recordsCountPerPage": 60,
    "priceMarketID": "24",
    "searchModeID": 2,
    "siteid": 24
}

url = 'https://www.tiffany.es/ecomproductsearchprocessapi/api/process/v1/productsearch/ecomguidedsearch'

# Realiza la solicitud POST con el cuerpo y encabezados configurados
response = requests.post(url, json=body, headers=headers)
# print(response.text)

data = json.loads(response.text)
print(data['resultDto']['dimensions'][0]['groupName'])

for name in data['resultDto']['dimensions']:
    print(name['groupName'])

