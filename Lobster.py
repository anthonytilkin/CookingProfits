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

        return buy_price_raw_lobster, sell_price_raw_lobster
    
def get_price_lobster():

    id_lobster = 379

    if str(id_lobster) in data['data']:
        data_lobster = data['data'][str(id_lobster)]
        buy_price_lobster = data_lobster.get('high')
        sell_price_lobster = data_lobster.get('low')

        print("\nLobster Prices:")
        print(f"Buy Price: {buy_price_lobster} coins")
        print(f"Sell Price: {sell_price_lobster} coins")

        return buy_price_lobster, sell_price_lobster
    
def get_profit_lobster(buy_raw, buy_cooked, sell_raw, sell_cooked):
    
    buy_buy_profit = buy_cooked - buy_raw
    buy_sell_profit = buy_cooked - sell_raw
    sell_buy_profit = sell_cooked - buy_raw
    sell_sell_profit = sell_cooked - sell_raw

    print("\nProfits Per Lobster:")
    print(f"Buy->Buy Profit: {buy_buy_profit} coins")
    print(f"Buy->Sell Profit: {buy_sell_profit} coins")
    print(f"Sell->Buy Profit: {sell_buy_profit} coins")
    print(f"Sell->Sell Profit: {sell_sell_profit} coins")

buy_raw, sell_raw = get_price_raw_lobster()
buy_cooked, sell_cooked = get_price_lobster()

get_profit_lobster(buy_raw, buy_cooked, sell_raw, sell_cooked)