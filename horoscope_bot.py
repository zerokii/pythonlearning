import os
import discord
import requests

from bs4 import BeautifulSoup

signs = {
    "aries": 1,
    "taurus": 2,
    "gemini": 3,
    "cancer": 4,
    "leo": 5,
    "virgo": 6,
    "libra": 7,
    "scorpio": 8,
    "sagittarius": 9,
    "capricorn": 10,
    "aquarius": 11,
    "pisces": 12,
}

class Horoscope:

    def __init__(self,current_date,description):
        self.current_date=current_date
        self.description=description

def get_horoscope(sign):
    url=f"https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign={signs.get(sign, '')}"

    response = requests.get(url)
    html = BeautifulSoup(response.text,'html.parser')
    container = html.find("p")

    split_message = container.text.strip().split(" - ")
    current_date = split_message[0]
    description = split_message[1]

    return Horoscope(current_date, description)

permissions = discord.Intents.default()
permissions.message_content = True

# represent bot
client = discord.Client(intents=permissions)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    # send message to each server it belongs to
    for guild in client.guilds:
        channel = guild.system_channel
        await channel.send(f"{client.user} is online!")

@client.event
async def on_message(message):

    if message.content.lower() in signs:
        sign= message.content.lower()
        sign_name = sign.title()
        horoscope = get_horoscope(sign)

        quote = f"Today's horoscope for {sign_name}: \n> " \
        f"Current date: {horoscope.current_date} \n> \n> " \
        f"{horoscope.description}"

        zodiac_image_path = os.path.join(os.path.dirname(__file__),f"images/{sign_name}.png")

        await message.channel.send(quote)
        await message.channel.send(file=discord.File(zodiac_image_path))

client.run(os.environ['TOKEN'])
