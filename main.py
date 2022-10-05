import os
from bs4 import BeautifulSoup
import requests
import telebot
import schedule
import time
API_KEY = '5758248073:AAHhRY67sCd7wDIbwTtJo6YMRNQFQfiE9dU'
bot = telebot.TeleBot(API_KEY)
channel = "@Quotes_P30"
url = requests.get('https://story-shack-cdn-v2.glitch.me/generators/quote-generator')

e = url.json()
j = e['data']['name']
#def post():
bot.send_message(channel,j)



def p1():
    schedule.every(30).minutes.until("19:00").do(post)

schedule.every().day.at("04:00").do(p1)

while True:
    schedule.run_pending()
    time.sleep(1) 

  

   
