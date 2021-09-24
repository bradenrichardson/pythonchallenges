import json
import requests
import argparse

## Challenges


# Braden
# 1. Create a program which allows a user to input any cryptocurrency ticker 
# and then receive an output of TRUE or FALSE as to whether that cryptocurrency
# is below the 50 Day EMA (Exponential Moving Average)
indicator = 'ema'

parser = argparse.ArgumentParser(description="A tool to calculate EMA and current price")
parser.add_argument('--ticker', type=str)
args = parser.parse_args()

nomics_api_key = 'd160787385b9f9db4ce21650dd01f92afdca78df'
taapi_api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImJyYWRlbi5yaWNoYXJkc29uMTNAZ21haWwuY29tIiwiaWF0IjoxNjMyMzIwMzIwLCJleHAiOjc5Mzk1MjAzMjB9.9LJDqh221DdMWZfdXwKtqXHlKkv_dq07L81NH3jUEZM'

paramaters = {
    'secret' : taapi_api_key,
    'exchange' : 'binance',
    'symbol' : args.ticker,
    'interval': '1d'
}

ticker_nude = args.ticker.split('/')

headers = {
    'key' : nomics_api_key 
}

def get_price():
    response = requests.get("https://api.nomics.com/v1/currencies/ticker?key={0}&ids={ticker}&interval=1d,30d&convert=EUR&per-page=100&page=1".format(nomics_api_key, ticker=ticker_nude[0]))
    json_response = response.json()
    print('PRICE : $' + str(json_response[0].get('price')))
    return float(json_response[0].get('price'))

    



def get_ema():
    response = requests.get(url= f"https://api.taapi.io/{indicator}", params=paramaters)
    json_response = response.json()
    print('EMA: $' + str(json_response.get('value')))
    return float(json_response.get('value'))



def main():

    if get_ema() > get_price():
        print('FALSE')
    elif get_ema() < get_price():
        print('TRUE')

main()