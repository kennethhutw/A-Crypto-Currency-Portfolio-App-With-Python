# https://github.com/kennethhutw/A-Crypto-Currency-Portfolio-App-With-Python
# Copyright (c) 2015 Kenneth Hu; Licensed MIT 
# Email : Kenneth.hu@hotmail.com
# Purpose : print crypto portfolio
import requests
import json
import os
os.system('cls')
################################################

api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
api = json.loads(api_request.content)

#currencies = ["BTC", "XRP", "EOS", "STEEM"]

my_portfolio = [
    {
        "sym": "STEEM",
        "amount_owned": 3000,
        "price_paid_per": .80
    },
    {
        "sym": "XRP",
        "amount_owned": 5000,
        "price_paid_per": .20
    },
    {
        "sym": "XLM",
        "amount_owned": 2000,
        "price_paid_per": .10
    },
    {
        "sym": "EOS",
        "amount_owned": 1000,
        "price_paid_per": 2.00
    }
]
portfolio_profit_loss = 0
for x in api:
    for coin in my_portfolio:
        if coin["sym"] == x["symbol"]:

            # Do math
            total_paid = float(coin["amount_owned"]) * float(coin["price_paid_per"])
            current_value = float(coin["amount_owned"]) * float(x["price_usd"])
            profit_loss = current_value - total_paid
            portfolio_profit_loss += profit_loss

            # Print detail info
            print(x["name"])
            print("${0:.2f}".format(float(x["price_usd"])))
            print("Rank : {0:.0f}".format(float(x["rank"])))
            print("Total Paid: {0:.2f}".format(float(total_paid)))
            print("Current Paid: {0:.2f}".format(float(current_value)))
            print("Profit/Loss: {0:.2f}".format(float(profit_loss)))
            print("----------------------------")

print("Portfolio Profit/Loss: ${0:2f}".format(float(portfolio_profit_loss)))


