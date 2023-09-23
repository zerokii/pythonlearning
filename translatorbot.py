import os
import discord
# from keep_alive import
from googletrans import Translator

BOT_PREFIX = "!"
DEST_LANG = "en"

translator = Translator()


def get_translation(message):
    translate = translator.translate(message, dest=DEST_LANG)
    translated = translate
    return translated.text


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
    if message.author == client.user:
        return

    print(message.content)

    if message.content.startswith(BOT_PREFIX):
        text = message.content.split(BOT_PREFIX + " ")
        str_text = map(str, text)
        list_to_str = "".join(str_text)

        detected_language = translator.detect(list_to_str).lang

        if detected_language == DEST_LANG:
            await message.channel.send(list_to_str)
        else:
            translated = get_translation(list_to_str)
            await message.channel.send(translated)

client.run("MTE1MjQzNTA2NDgzMjAwODIxMw.Gkybn6.Q5CkPcGk_dVynCPW3U7Va0BMpbq5lxfpw5RNe0")
