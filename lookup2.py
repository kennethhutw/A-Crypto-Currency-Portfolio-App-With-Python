# https://github.com/kennethhutw/A-Crypto-Currency-Portfolio-App-With-Python
# Copyright (c) 2015 Kenneth Hu; Licensed MIT 
# Email : Kenneth.hu@hotmail.com
# Purpose : print data by the list of currency
import requests
import json
import os
os.system('cls')
################################################

api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
api = json.loads(api_request.content)

currencies = ["BTC", "ETH", "XRP", "EOS", "STEEM"]

for x in api:
    for coin in currencies:
        if coin == x["symbol"]:
            print(x["name"])
            print(x["price_usd"])
            print(x["rank"])
            print("----------------------------")


