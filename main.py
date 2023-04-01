from PIL import Image,ImageFont,ImageDraw
image = Image.open("demo.jpg")

font = ImageFont.truetype("arial.ttf",24)
draw = ImageDraw.Draw(image)




import os
from bs4 import BeautifulSoup
import requests
import telebot
import schedule
import time
API_KEY = '5758248073:AAHhRY67sCd7wDIbwTtJo6YMRNQFQfiE9dU'
bot = telebot.TeleBot(API_KEY)
channel = "@Quotes_P30"
channel2 = "@eyobmekonneny"

def post():
  url = requests.get('https://story-shack-cdn-v2.glitch.me/generators/quote-generator')

  e = url.json()

  j = e['data']['name']
  bot.send_message(channel,j +'\n\U0001f31a | @Quotes_P30')

  text = str(j)
  draw.text((0,150), text,(0,0,10), font=font)
  image.save("teddxnnnnt.png")
  bot.send_photo(channel, image, caption=j) 


post();
