from PIL import Image,ImageFont,ImageDraw
image = Image.open("demo.jpg")
import textwrap
import random
font = ImageFont.truetype("mine.TTF",60)
draw = ImageDraw.Draw(image)
fontlogo = ImageFont.truetype("mine.TTF",40)



import os
from bs4 import BeautifulSoup
import requests
import telebot
import schedule
import time
API_KEY ='5758248073:AAHhRY67sCd7wDIbwTtJo6YMRNQFQfiE9dU'
bot = telebot.TeleBot(API_KEY)
channel = "@Quotes4_life"
channel2 = "@eyobmekonneny"

def post():
    url = requests.get('https://story-shack-cdn-v2.glitch.me/generators/quote-generator')

    e = url.json()

    j = e['data']['name']
    logo = "TG : @Quotes4_life \n IG : @Quotes4_life_official"
    text = str(j)

    para = textwrap.wrap(j, width=15)
    red = random.randint(0,255)
    blue = random.randint(0,255)
    green = random.randint(0,255)
    MAX_W, MAX_H = 2000, 2000
    image = Image.new('RGB', (MAX_W, MAX_H), (red, green, blue, 0))

 
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("mine.TTF", 180)
    
    current_h, pad = 500, 10
    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text(((MAX_W - w) / 2, current_h), line, font=font)
        current_h += h + pad
    
    draw.text((1500,1900), logo,(255,255,255), font=fontlogo)
    image.save("teddxnnnnt.png")
    bot.send_photo(channel, image, caption=j + '\n\U0001f31a | @Quotes4_life') 
    bot.send_photo(channel2, image, caption=j + '\n\U0001f31a | @Quotes4_life') 
    
def p1():
    schedule.every(120).minutes.until("19:00").do(post)
schedule.every().day.at("04:00").do(p1)
while True:
    schedule.run_pending()
    time.sleep(1)
