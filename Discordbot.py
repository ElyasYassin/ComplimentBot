import random
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')


# Compliments about Elyas
COMPLIMENTS = [
    "Elyas is the kind of person who makes every project feel possible. 🔥",
    "If brilliance had a face, it would look a lot like Elyas.",
    "Elyas doesn’t chase greatness—greatness chases Elyas.",
    "Elyas is proof that hustle and heart get you far.",
    "Every server is lucky to have Elyas in it 💯",
    "Some people talk the talk. Elyas walks it, builds the sidewalk, and paves the future.",
]

# Set up bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s).")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.tree.command(name="complimentelyas", description="Get a legendary compliment about Elyas")
async def complimentelyas(interaction: discord.Interaction):
    compliment = random.choice(COMPLIMENTS)
    await interaction.response.send_message(compliment)

bot.run(TOKEN)