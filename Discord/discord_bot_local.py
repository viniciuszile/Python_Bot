from discord.ext import commands
from datetime import date
import discord
from bs4 import BeautifulSoup
import requests
import urllib.parse
import random
import asyncio


# Obter a data atual
data_atual = date.today().strftime('%d-%m-%Y')

# Carrega o token de autenticação do arquivo
token = ''

# Define os intents que o bot vai utilizar
intents = discord.Intents.default()
intents.messages = True  # Enable receiving message events

# Cria uma instância do bot com os intents
bot = commands.Bot(command_prefix='!', intents=intents)

# ID do canal de destino
channel_id = 1114784923962839132

# Evento de inicialização
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Comando inválido", color=discord.Color.red())
        embed.add_field(name="Comando não encontrado", value="Digite $comandos para ver a lista de comandos disponíveis.", inline=False)
        await ctx.send(embed=embed)

@bot.command()
async def b(ctx):
    embed = discord.Embed(title="**Buscar Jogador**", color=discord.Color.blue())
    embed.add_field(name="Digite o nickname (ex: zile):", value="Aguardando entrada...", inline=False)
    await ctx.send(embed=embed)

    nickname_msg = await bot.wait_for("message", check=lambda message: message.author == ctx.author)
    nickname = nickname_msg.content

    embed.set_field_at(0, name="Digite o ID (ex: FEC):", value="Aguardando entrada...")
    await ctx.send(embed=embed)

    id_msg = await bot.wait_for("message", check=lambda message: message.author == ctx.author)
    id_ = id_msg.content
    if not id_.startswith("#"):
        id_ = "#" + id_

    formatted_nickname = urllib.parse.quote_plus(nickname)
    formatted_id = urllib.parse.quote_plus(id_)
    formatted_id = formatted_id.replace('#', '%23')

    base_url = 'https://tracker.gg/valorant/profile/riot/'
    profile_url = f'{base_url}{formatted_nickname}{formatted_id}/overview'

    response = requests.get(profile_url)
    content = response.content

    soup = BeautifulSoup(content, 'html.parser')
    div_elements = soup.find_all('div', class_='value')

    if len(div_elements) >= 2:
        rank_atual = div_elements[0].get_text(strip=True)
        maior_rank = div_elements[1].get_text(strip=True)
        boneco_div = soup.find('div', class_='value', set=True)
        boneco = boneco_div.text.strip() if boneco_div else 'N/A'

        embed = discord.Embed(title="**Informações do Jogador**", color=discord.Color.blue())
        embed.add_field(name="Rank atual:", value=rank_atual + " 🏆", inline=False)
        embed.add_field(name="Maior rank alcançado:", value=maior_rank + " 🐐", inline=False)
        embed.add_field(name="Boneco mais jogado:", value=boneco + " 🎯", inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send('Não foi possível encontrar os dados do rank.')


@bot.command()
async def buscar(ctx):
    embed = discord.Embed(title="**Buscar Jogador**", color=discord.Color.blue())
    embed.add_field(name="Digite o nickname (ex: zile):", value="Aguardando entrada...", inline=False)
    await ctx.send(embed=embed)

    nickname_msg = await bot.wait_for("message", check=lambda message: message.author == ctx.author)
    nickname = nickname_msg.content

    embed.set_field_at(0, name="Digite o ID (ex: FEC):", value="Aguardando entrada...")
    await ctx.send(embed=embed)

    id_msg = await bot.wait_for("message", check=lambda message: message.author == ctx.author)
    id_ = id_msg.content
    if not id_.startswith("#"):
        id_ = "#" + id_

    formatted_nickname = urllib.parse.quote_plus(nickname)
    formatted_id = urllib.parse.quote_plus(id_)
    formatted_id = formatted_id.replace('#', '%23')

    base_url = 'https://tracker.gg/valorant/profile/riot/'
    profile_url = f'{base_url}{formatted_nickname}{formatted_id}/overview'

    response = requests.get(profile_url)
    content = response.content

    soup = BeautifulSoup(content, 'html.parser')
    div_elements = soup.find_all('div', class_='value')

    if len(div_elements) >= 2:
        rank_atual = div_elements[0].get_text(strip=True)
        maior_rank = div_elements[1].get_text(strip=True)
        boneco_div = soup.find('div', class_='value', set=True)
        boneco = boneco_div.text.strip() if boneco_div else 'N/A'

        embed = discord.Embed(title="**Informações do Jogador**", color=discord.Color.blue())
        embed.add_field(name="Rank atual:", value=rank_atual + " 🏆", inline=False)
        embed.add_field(name="Maior rank alcançado:", value=maior_rank + " 🐐", inline=False)
        embed.add_field(name="Boneco mais jogado:", value=boneco + " 🎯", inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send('Não foi possível encontrar os dados do rank.')


# Executa o bot
bot.run(token)
