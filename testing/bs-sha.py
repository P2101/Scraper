import requests
from bs4 import BeautifulSoup

def getSha(json):
    shas = []
    for a in json:
        pass
    pass


# Busca en Codigo Fuente el JSON  donde están los SHAs
def requestGraphQL():
    # pregmatch para obtener el json. SHA está dentro de cacheHints
    # if del template[data-varname=...... hasta el else
    
    json = json.decode('utf-8')
    pass

# Buscarlos en la web
provider = 'vtex.admin-graphql-ide@3.x'
sender = 'vtex.admin-graphql-ide@3.x'
