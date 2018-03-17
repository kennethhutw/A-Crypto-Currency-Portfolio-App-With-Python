# https://github.com/kennethhutw/A-Crypto-Currency-Portfolio-App-With-Python
# Copyright (c) 2015 Kenneth Hu; Licensed MIT 
# Email : Kenneth.hu@hotmail.com
# Purpose : Get data from coinmarketcap 
import requests
import json
import os
os.system('cls')

#########################################3

api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
api = json.loads(api_request.content)

print(api)