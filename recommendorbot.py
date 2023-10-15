import os
import discord

MEAL_CHOICES = {
    "$breakfast": ["sandwich", "salad"],
    "$lunch": ["spaghetti", "tacos"],
    "$dinner": ["sushi", "french fries"],
}


def get_recommendation(text):
    for meal, choices in MEAL_CHOICES.items():
        if text.startswith(meal):
            choice_number = text.split(meal)[-1].strip()

            try:
                choice = choices[int(choice_number) - 1]
            except(ValueError, IndexError):
                choice = "invalid choice, please use 1 or 2"

            return choice


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
    text = message.content.lower()

    if text.startswith("$hello"):
        response = "hello!\n> welcome to meal recommender system\n> " \
                   "$breakfast / $lunch / $dinner\n> " \
                   "1: food / 2: snack\n> " \
                   "e.g.: $breakfast 2"

        await message.channel.send(response)

    else:
        choice = get_recommendation(text)

        if choice is not None:
            recommendation = "food recommendation: " + choice

            food_image_path = os.path.join(os.path.dirname(__file__), f'images/{choice}.png')

            await message.channel.send(recommendation)
            await message.channel.send(file=discord.File(food_image_path))


client.run(os.environ["TOKEN"])
