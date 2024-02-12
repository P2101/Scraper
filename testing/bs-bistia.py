import requests
from bs4 import BeautifulSoup
# import mail
import time
import re

# BOOKING
# url = 'https://www.booking.com/hotel/hu/city-center-historic-jewish-quarter.es.html?aid=356980&label=gog235jc-1FCAMYkwQoZzjxAkgKWANoRogBAZgBCrgBGMgBDNgBAegBAfgBAogCAagCBLgC9NjKngbAAgHSAiRkYjc0Y2E5Ny1iODkxLTQ5ODAtOTk2MS1lMTljOWQ5ZTllMTXYAgXgAgE&sid=3ecb85af54446a94a4e966417939cf16&all_sr_blocks=881525201_357422493_8_0_0;checkin=2023-04-07;checkout=2023-04-09;dest_id=-850553;dest_type=city;dist=0;group_adults=8;group_children=0;hapos=5;highlighted_blocks=881525201_357422493_8_0_0;hpos=5;matching_block_id=881525201_357422493_8_0_0;no_rooms=1;req_adults=8;req_children=0;room1=A%2CA%2CA%2CA%2CA%2CA%2CA%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=881525201_357422493_8_0_0__56033;srepoch=1674751123;srpvid=295a7509cc290006;type=total;ucfs=1&#hotelTmpl'
url = 'https://www.booking.com/hotel/hu/rackozi-apt.es.html?aid=356980&label=gog235jc-1FCAMYkwQoZzjxAkgKWANoRogBAZgBCrgBGMgBDNgBAegBAfgBAogCAagCBLgC9NjKngbAAgHSAiRkYjc0Y2E5Ny1iODkxLTQ5ODAtOTk2MS1lMTljOWQ5ZTllMTXYAgXgAgE&sid=c6dc4e32761a1d6a0bccab8814164634&all_sr_blocks=654449301_267917665_8_0_0;checkin=2024-05-15;checkout=2024-05-17;dest_id=-850553;dest_type=city;dist=0;group_adults=8;group_children=0;hapos=7;highlighted_blocks=654449301_267917665_8_0_0;hpos=7;matching_block_id=654449301_267917665_8_0_0;no_rooms=1;req_adults=8;req_children=0;room1=A%2CA%2CA%2CA%2CA%2CA%2CA%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=654449301_267917665_8_0_0__26880;srepoch=1706259157;srpvid=f3a03e5e42180035;type=total;ucfs=1&#hotelTmpl'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

def get_old_price(html: BeautifulSoup):
    lines = html.select('table#hprt-table tbody tr')
    print(len(lines))
    # for row in lines:
    #     row: BeautifulSoup
    #     name = row.select_one('.hprt-roomtype-icon-link').text.strip()
    #     print(f"El nombre es {name}")

    #     bui_f_color_destructive = row.select_one('.bui-f-color-destructive')
    #     if bui_f_color_destructive is not None:
    #         old_price = bui_f_color_destructive.text.strip()
    #         print(f"El precio viejo es {old_price}")
    #     else:
    #         print('no tiene precio antiguo')

    #     new_price = row.select_one('.bui-price-display__value.prco-inline-block-maker-helper').text.strip()
    #     print(f"El precio nuevo es {new_price}")
    for row in lines:
        row: BeautifulSoup

        # Verificar si se encontró el elemento '.hprt-roomtype-icon-link'
        roomtype_icon_link = row.select_one('.hprt-roomtype-icon-link')
        if roomtype_icon_link:
            name = roomtype_icon_link.text.strip()
            print(f"El nombre es {name}")
        else:
            print("No se encontró '.hprt-roomtype-icon-link' en esta fila")

        # Verificar si se encontró el elemento '.bui-f-color-destructive'
        bui_f_color_destructive = row.select_one('.bui-f-color-destructive')
        if bui_f_color_destructive:
            old_price = bui_f_color_destructive.text.strip()
            print(f"El precio viejo es {old_price}")
        else:
            print('No tiene precio antiguo')

        new_price = row.select_one('.bui-price-display__value.prco-inline-block-maker-helper').text.strip()
        print(f"El precio nuevo es {new_price}")


# def get_old_price(html: BeautifulSoup):
    # lines = html.select('table#hprt-table tbody tr')
    # print(len(lines))
    # for row in lines:
    #     row: BeautifulSoup
    #     roomtype_icon_link = row.select_one('.hprt-roomtype-icon-link')
    #     if roomtype_icon_link is not None:
    #         name = roomtype_icon_link.text.strip()
    #         print(f"El nombre es {name}")

    #     old_prices = row.select_one('.bui-f-color-destructive')
    #     if old_prices is not None:
    #         old_price = old_prices.text.strip()
    #         print(f"El precio viejo es {old_price}")
    #     else:
    #         print('Noo tiene precio antiguo')

    #     new_price = row.select_one('.bui-price-display__value.prco-inline-block-maker-helper')
    #     if new_price is not None:
    #         new_price_text = new_price.text.strip()
    #         print(f"El precio nuevo es {new_price_text}")
    #     else:
    #         print('no tiene precio nuevo')

# def get_old_price(html: BeautifulSoup):
#     prices = html.select('.bui-u-sr-only')
#     for price in prices:
#         if 'Precio' in price:
#             valores = re.findall(r'€ (\d+)', price)
#             # Si hay al menos dos valores encontrados, tomamos el primero como el precio original y el segundo como el precio actual
#             if len(valores) >= 2:
#                 precio_original = int(valores[0])
#                 precio_actual = int(valores[1])

#                 print("Precio original:", precio_original)
#                 print("Precio actual:", precio_actual)
#                 # break
#             else:
#                 print("No se encontraron suficientes valores numéricos.")
# def get_old_price(html: BeautifulSoup):
#     # Buscar el elemento que contiene la palabra 'Precio'
#     span = html.find('span', class_='bui-u-sr-only')

#     if span:
#         # Extrae el texto del span
#         span_text = span.get_text()

#         # Busca los valores numéricos precedidos por el símbolo Euro (€)
#         valores = re.findall(r'€ (\d+)', span_text)

#         if len(valores) >= 2:
#             precio_original = int(valores[0])
#             precio_actual = int(valores[1])

#             print("Precio original:", precio_original)
#             print("Precio actual:", precio_actual)
#         else:
#             print("No se encontraron suficientes valores numéricos.")
#     else:
#         print("No se encontró el span con la clase 'bui-u-sr-only'.")


def get_price(html: BeautifulSoup):
    # old_prices = html.find('div', {'class': 'bui-f-color-destructive'}).text
    # print(f"olddd ", old_prices)
    try:
        prices = html.find('span', {'class': 'prco-valign-middle-helper'}).text
        new_price = re.search(r'€ \d+', prices)
        print(f"new ", new_price)
        return new_price
    except AttributeError as ae:
        print(ae), "\skipping line:"
    except IndexError as ie:
        print(ie), "\skipping line:"

def check_price():
    current_price = get_price()
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find("title").text.encode('utf-8')
    print(f"The apartement is {title}")
    message = f"El precio ha bajado => {current_price} ", url
    # mail.send_mail(message, title)

# Function for reading the TXT FILE
def readFile():
    f = open("price.txt", "r")
    if f.mode == 'r':
        content = f.read()
    f.close()
    return content

# FUNCTION FOR WRITING ON THE TXT FILE
def writeFile(number):
    f = open("price.txt", "w")
    if f.mode == 'w':
        f.write(number)
    f.close()

# MAIN FUNCTION
def main():
    page = requests.get(url, headers=headers)
    html = BeautifulSoup(page.content, "html.parser")
    get_old_price(html)

if __name__ == '__main__':
    main()
