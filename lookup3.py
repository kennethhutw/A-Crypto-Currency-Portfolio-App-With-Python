# https://github.com/kennethhutw/A-Crypto-Currency-Portfolio-App-With-Python
# Copyright (c) 2015 Kenneth Hu; Licensed MIT 
# Email : Kenneth.hu@hotmail.com
# Purpose : format the value
import requests
import json
import os
os.system('cls')
################################################

api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
api = json.loads(api_request.content)

currencies = ["BTC", "XRP", "EOS", "STEEM"]

for x in api:
    for coin in currencies:
        if coin == x["symbol"]:
            print(x["name"])
            print("${0:.2f}".format(float(x["price_usd"])))
            print("Rank : {0:.0f}".format(float(x["rank"])))
            print("----------------------------")


