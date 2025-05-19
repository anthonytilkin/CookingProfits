import requests

url = "https://prices.runescape.wiki/api/v1/osrs/latest"

response = requests.get(url)
data = response.json()

def get_price_raw_lobster():

    id_raw_lobster = 377

    if str(id_raw_lobster) in data['data']:
        data_raw_lobster = data['data'][str(id_raw_lobster)]
        buy_price_raw_lobster = data_raw_lobster.get('high')
        sell_price_raw_lobster = data_raw_lobster.get('low')

        print("Raw Lobster Prices:")
        print(f"Buy Price: {buy_price_raw_lobster} coins")
        print(f"Sell Price: {sell_price_raw_lobster} coins")

def get_price_lobster():

    id_lobster = 379

    if str(id_lobster) in data['data']:
        data_lobster = data['data'][str(id_lobster)]
        buy_price_lobster = data_lobster.get('high')
        sell_price_lobster = data_lobster.get('low')

        print("Lobster Prices:")
        print(f"Buy Price: {buy_price_lobster} coins")
        print(f"Sell Price: {sell_price_lobster} coins")


get_price_raw_lobster()
get_price_lobster()