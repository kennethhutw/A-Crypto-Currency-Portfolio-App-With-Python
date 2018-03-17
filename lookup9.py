# https://github.com/kennethhutw/A-Crypto-Currency-Portfolio-App-With-Python
# Copyright (c) 2015 Kenneth Hu; Licensed MIT 
# Email : Kenneth.hu@hotmail.com
# Purpose : add rows
from Tkinter import * 
import requests
import json
import os
os.system('cls')
################################################

root = Tk()


root.title("Crypto Currency Portfolio")
root.iconbitmap(r'./portfolio.ico')

# ************** CREATE HEADER  ****************
#header = ["Name", "Rank", "Current Price", "Price Paid", "P/L Per", "1-Hour Change", "24-Hour Change", "7-Day Change","Current Value", "P/L Total"]

header_name = Label(root, text="Name", bg="blue", fg="white" )
header_name.grid(row=0, column=0, sticky=N+S+E+W)

header_rank = Label(root, text="Rank", bg="blue", fg="white" )
header_rank.grid(row=0, column=1, sticky=N+S+E+W)

header_current_price = Label(root, text="Current Price", bg="blue", fg="white" )
header_current_price.grid(row=0, column=2, sticky=N+S+E+W)

header_price_paid = Label(root, text="Price Paid", bg="blue", fg="white")
header_price_paid.grid(row=0, column=3, sticky=N+S+E+W)

header_profit_loss_per = Label(root, text="Profit/Loss Per", bg="blue", fg="white")
header_profit_loss_per.grid(row=0, column=4, sticky=N+S+E+W)

header_1_hr_change = Label(root, text="1 HR Change", bg="blue", fg="white" )
header_1_hr_change.grid(row=0, column=5, sticky=N+S+E+W)

header_24_hr_change = Label(root, text="24-Hour Change", bg="blue", fg="white" )
header_24_hr_change.grid(row=0, column=6, sticky=N+S+E+W)

header_7_day_change = Label(root, text="7-Day Change", bg="blue", fg="white" )
header_7_day_change.grid(row=0, column=7, sticky=N+S+E+W)

header_current_value = Label(root, text="Current Value", bg="blue", fg="white" )
header_current_value.grid(row=0, column=8, sticky=N+S+E+W)

header_profit_loss_total = Label(root, text="Profit/Loss Total", bg="blue", fg="white" )
header_profit_loss_total.grid(row=0, column=9, sticky=N+S+E+W)
# ************** END HEADER  SECTION ****************





#currencies = ["BTC", "XRP", "EOS", "STEEM"]


portfolio_profit_loss = 0

print("----------------------------")

def lookup():
    api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")
    api = json.loads(api_request.content)
    # My Portfolio
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
    row_count = 1
    for x in api:
        for coin in my_portfolio:
            if coin["sym"] == x["symbol"]:

                # Do some math
                total_paid = float(coin["amount_owned"]) * float(coin["price_paid_per"])
                current_value = float(coin["amount_owned"]) * float(x["price_usd"])
                profit_loss = current_value - total_paid
                portfolio_profit_loss += profit_loss
                profit_loss_per_coin = float(x["price_usd"]) - float(coin["price_paid_per"])

                print(x["name"])
                print(" Current Price: ${0:.2f}".format(float(x["price_usd"])))
                print(" Profit/Loss per Coin: ${0:.2f}".format(float(profit_loss_per_coin)))
                print(" Rank : {0:.0f}".format(float(x["rank"])))
                print(" Total Paid: {0:.2f}".format(float(total_paid)))
                print(" Current Paid: {0:.2f}".format(float(current_value)))
                print(" Profit/Loss: {0:.2f}".format(float(profit_loss)))
                print("----------------------------")


                name = Label(root, text="Name", bg="white" )
                name.grid(row=row_count, column=0, sticky=N+S+E+W)

                rank = Label(root, text="Rank", bg="silver" )
                rank.grid(row=row_count, column=1, sticky=N+S+E+W)

                current_price = Label(root, text="Current Price" )
                current_price.grid(row=row_count, column=2, sticky=N+S+E+W)

                price_paid = Label(root, text="Price Paid", bg="silver")
                price_paid.grid(row=row_count, column=3, sticky=N+S+E+W)

                profit_loss_per = Label(root, text="Profit/Loss Per", bg="white")
                profit_loss_per.grid(row=row_count, column=4, sticky=N+S+E+W)

                one_hr_change = Label(root, text="1 HR Change", bg="silver" )
                one_hr_change.grid(row=row_count, column=5, sticky=N+S+E+W)

                tf_hr_change = Label(root, text="24-Hour Change", bg="white" )
                tf_hr_change.grid(row=row_count, column=6, sticky=N+S+E+W)

                seven_day_change = Label(root, text="7-Day Change", bg="silver" )
                seven_day_change.grid(row=row_count, column=7, sticky=N+S+E+W)

                current_value = Label(root, text="Current Value", bg="white" )
                current_value.grid(row=row_count, column=8, sticky=N+S+E+W)

                profit_loss_total = Label(root, text="Profit/Loss Total", bg="silver" )
                profit_loss_total.grid(row=row_count, column=9, sticky=N+S+E+W)

                row_count += 1

    print("Portfolio Profit/Loss: ${0:2f}".format(float(portfolio_profit_loss)))
lookup()

root.mainloop()

