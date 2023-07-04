import requests
from bs4 import BeautifulSoup
import mail
import time
import re

# BOOKING EXAMPLE 
url = 'https://www.booking.com/hotel/hu/city-center-historic-jewish-quarter.es.html?aid=356980&label=gog235jc-1FCAMYkwQoZzjxAkgKWANoRogBAZgBCrgBGMgBDNgBAegBAfgBAogCAagCBLgC9NjKngbAAgHSAiRkYjc0Y2E5Ny1iODkxLTQ5ODAtOTk2MS1lMTljOWQ5ZTllMTXYAgXgAgE&sid=3ecb85af54446a94a4e966417939cf16&all_sr_blocks=881525201_357422493_8_0_0;checkin=2023-04-07;checkout=2023-04-09;dest_id=-850553;dest_type=city;dist=0;group_adults=8;group_children=0;hapos=5;highlighted_blocks=881525201_357422493_8_0_0;hpos=5;matching_block_id=881525201_357422493_8_0_0;no_rooms=1;req_adults=8;req_children=0;room1=A%2CA%2CA%2CA%2CA%2CA%2CA%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=881525201_357422493_8_0_0__56033;srepoch=1674751123;srpvid=295a7509cc290006;type=total;ucfs=1&#hotelTmpl'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

def get_old_price(html: BeautifulSoup):
    # WE EXTRACT THE TDs
    lines = html.select('table#hprt-table tbody tr')
    for row in lines:
        row: BeautifulSoup
        if row.select_one('.bui-f-color-destructive') == None:
            print('DOESN\'T HAVE ANY OFFER')
        else:
            old_price = row.select_one('.bui-f-color-destructive').text.strip()
            # WE CHECK WHERE WE HAVE THE SIGN OF DOLAR/EURO, AND WE DELETE IT
            if re.search('^[€|$]', old_price):
                price = old_price[2:]
            else:
                price = old_price[:-2]
            return float(price)

def get_price(html: BeautifulSoup):
    lines = html.select('table#hprt-table tbody tr')
    for row in lines:
        row: BeautifulSoup
        new_price = row.select_one('.bui-price-display__value.prco-inline-block-maker-helper').text.strip()
        if re.search('^[€|$]', new_price):
            price = new_price[2:]
        else:
            price = new_price[:-2]
        return float(price)

def get_name(html: BeautifulSoup):
    lines = html.select('table#hprt-table tbody tr')
    for row in lines:
        row: BeautifulSoup
        name = row.select_one('.hprt-roomtype-icon-link').text.strip().encode('utf-8')
        return name

# MAIN FUNCTION
def check_price():
    # HERE WE GOT THE HTML
    page = requests.get(url, headers=headers)
    html = BeautifulSoup(page.content, "html.parser")

    # WE CALL THE FUNCTIONS
    old_price = get_old_price(html)
    new_price = get_price(html)
    name = get_name(html)

    # IF THE PRICE GOES DOWN, WE SEND A MESSAGE
    if old_price == None:
        message = f"The apartement {name} is => {new_price} €", url
    elif new_price < old_price:
        message = f"The apartement {name} has gone down from {old_price} => {new_price} ", url
        mail.send_mail(message, name)

# INFINITE LOOP, RUNS AND CHECKS THE PRICE EVERY 7H
while (True):
    check_price()
    # WE CHECK THE WEB SITE EVERY 7H
    time.sleep((60 * 60) * 7)
