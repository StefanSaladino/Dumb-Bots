import discord
from dotenv import load_dotenv
import os
from discord.ext import commands
import random

with open('token.env', 'r') as file:
    TOKEN = file.read().strip()

# Retrieve guild name from guild.env file
with open('guild.env', 'r') as file:
    GUILD_NAME = file.read().strip()

with open('guild2.env', 'r') as file:
    GUILD_NAME_2 = file.read().strip()

TARGET_WORD = 'java'
IMAGE_FILENAME = 'java-hd.jpeg'
IMAGE2_FILENAME = 'java-SB.jpg'
IMAGE3_FILENAME = 'Java-IQ.png'
GIF_FILENAME = 'Java-gif.gif'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hotDog(message):
    if message.author == bot.user:
        return
    await message.channel.send("Who hath summoned the Java hot dog?")
    with open(IMAGE_FILENAME, 'rb') as file:
        picture = discord.File(file)
        await message.channel.send(file=picture)

    # Ignore messages sent by the bot itself
    
@bot.command() 
async def spongeBob(message):
    # Ignore messages sent by the bot itself
    user_tag = message.author.mention
    if message.author == bot.user:
        return
    await message.channel.send(f"Congrats {user_tag}, you've unlocked the secret Java meme!")
    with open(IMAGE2_FILENAME, 'rb') as file:
        picture = discord.File(file)
        await message.channel.send(file=picture)

@bot.command()
async def jIQ(message):
    if message.author == bot.user:
        return
    await message.channel.send("FYI, I was coded in the language on the left!")
    with open(IMAGE3_FILENAME, 'rb') as file:
        picture = discord.File(file)
        await message.channel.send(file=picture)

@bot.command()
async def javaGIF(message):
    if message.author == bot.user:
        return
    await message.channel.send("Java? Allow this GIF to explain.")
    with open(GIF_FILENAME, 'rb') as file:
        picture = discord.File(file)
        await message.channel.send(file=picture)

    
@bot.event
async def on_message(message):
    if message.author==bot.user:
        return
    if TARGET_WORD.lower() in message.content.lower():
        # Check if the message is in a text channel
        random_number = random.randint(1, 101)
        if random_number <= 33:
            await hotDog(message)
        elif 34 <= random_number <= 66:
            await jIQ(message)
        elif 67 <= random_number <= 99:
            await javaGIF(message)
        else:
            await spongeBob(message)

bot.run(TOKEN)