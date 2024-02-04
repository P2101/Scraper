# Si tenemos un POST y nos pide un SHA, ese SHA está en el código fuente y debemos proporcionar ese provider y sender para poder guardarlo
# FALTARIA TODAVÍA CREAR LA FUNCIÓN GETREQUESTGRAPHQL Y GUARDAR EL SHA EN EL ARRAY SHAS


import re
import requests
from bs4 import BeautifulSoup
import json 

# url = 'https://www.guess.mx/'
# proxy = {'http': '45.174.87.18'}  

# headers = {
#    'authority': 'www.guess.mx',
#    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#    'accept-language': 'es-ES,es;q=0.9,en;q=0.8,ca;q=0.7',
#    'cache-control': 'max-age=0',
#    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
# }

# response = requests.get(url, headers=headers, proxies=proxy).text
# soup = BeautifulSoup(response, 'html.parser')
# print(soup)

# Normalmente nos lo pide un POST
def getSha(json_data):
    shas = []
    # Buscarlos en la web, network COPIAR los que nos pide el POST
    real_provider = 'vtex.admin-graphql-ide@3.x'
    real_sender = 'vtex.admin-graphql-ide@3.x'
    data = json_data.get('cacheHints', [])

    for sha, details in data.items():
        if "provider" in details and "sender" in details:
            if real_provider == details["provider"] and real_sender == details['sender']:
                print(f"SHA: {sha}")
        # else:
        #     print(f"Invalid format for SHA {sha}")

# def requestGraphQL(json): # sería aquesta funció
# Abre el archivo JSON y maneja posibles errores de decodificación
shas_file = 'sha.json' 
with open(shas_file, 'r', encoding='utf-8') as file:
    try:
        data = json.load(file)
        # Ahora, 'data' contiene el contenido del archivo JSON como un diccionario en Python
        getSha(data)
    except json.JSONDecodeError as e:
        print(f"Error al decodificar el archivo JSON: {e}")

