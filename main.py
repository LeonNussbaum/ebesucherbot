import requests
import os
from telegram.bot import Bot
import statistics
from datetime import date
import time
import json

VARIABLES_FILE = "variables.txt"

if not os.path.exists(VARIABLES_FILE):
    import setup
    setup.main()

with open("variables.txt", "r") as file:
    values = json.load(file)

telegram_token = values["telegram_token"]
chat_id = values["chat_id"]
os.environ["telegramtoken"] = telegram_token
auth = (values["login"] ,values["api_key"])
bot = Bot(token=os.environ["telegramtoken"])
base_url = "https://www.ebesucher.de/api/"

def getdata(date):
    query = {"timezone": "Europe/Berlin"}
    response = requests.get(f"{base_url}visitor_exchange.json/account/earnings_hourly/{date}", auth=auth, params=query)
    return list(response.json().items())

def getavg(items):
    values = []
    for key, value in items:
        values.append(value)
    print(values)
    return statistics.mean(values)

def sendemergencymsg(avg):
    message = "DER DURSCHNITT IN DEN LETZTEN 24 STUNDEN BETRAG : " + str(avg) + " MINI PC CHECKEN !"
    bot.send_message(chat_id=chat_id, text=message)

def sendnormalmsg(values):
    message = "Der Punkteaustoß betrag in den letzten 24 Stunden : " + str(values) + " Alles ok !"
    bot.send_message(chat_id=chat_id, text=message)   

while True:
    if time.strftime("%H:%M") == "23:58":
        items = getdata(date.today())
        avg = getavg(items)
        if avg < 500:
            sendemergencymsg(avg)
        else:
            sendnormalmsg(items)
    time.sleep(60)