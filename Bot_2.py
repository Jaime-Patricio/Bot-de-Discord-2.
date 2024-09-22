import discord
import random
from discord.ext import commands

choices = (".","wahaha","no se")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', help_command = commands.DefaultHelpCommand(
    no_category = "Comandos"

), intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def hello(ctx):
    """Solo es el bot que saluda."""
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    """Suena como si fuera Sans hablando."""
    await ctx.send("he" * count_heh)

@bot.command()
async def repite_lo_que_digo(ctx, content='YAAAAAAAAAAAAAAAAHOYAAAAAAA'):
    for i in range(5):
        """Ya es muy obvio. ._."""
        await ctx.send(content)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, choices =(choices)):
    """Un tipo dado, escoge un carácter puesto del código."""
    await ctx.send(random.choice(choices))

bot.run("Aquí iría el token.")
