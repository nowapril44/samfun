import requests
from bs4 import BeautifulSoup
import telebot
import time

bot = telebot.TeleBot("5624335999:AAFImjmCT3CUJZaarubyNfvgreJirDpdGWs")

url = "https://www.generatorslist.com/random/text/random-joke-generator"
payload = {"numResults": "3", "jokeType": "all"}

def get_jokes():
    response = requests.post(url, data=payload)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(class_="col-sm-12 col-lg-4 mb-4")
    jokes = []
    for element in elements:
        jokes.append(element.text)
    return jokes

while True:
    jokes = get_jokes()
    for joke in jokes:
        bot.send_message("@funwithchatgpt", joke)
    time.sleep(10)
