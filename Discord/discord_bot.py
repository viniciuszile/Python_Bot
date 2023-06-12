from discord.ext import commands
from datetime import date
import asyncio
import io
import random
import discord
import requests

# Obter a data atual
data_atual = date.today().strftime('%d-%m-%Y')

# Carrega o token de autenticação do arquivo
token = 's'

# Define os intents que o bot vai utilizar
intents = discord.Intents.default()
intents.messages = True  # Enable receiving message events

# Cria uma instância do bot com os intents
bot = commands.Bot(command_prefix='$', intents=intents)

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
async def comandos(ctx):
    embed = discord.Embed(title="**Comandos disponíveis**", color=discord.Color.blue())

    embed.add_field(name="`$comandos 📝`", value="Lista todos os comandos disponíveis.", inline=False)
    embed.add_field(name="`$rank 🏆`", value="Ver todos os ranks.", inline=False)
    embed.add_field(name="`$rank_user 🥇`", value="Ver rank individual.", inline=False)
    embed.add_field(name="`$opniao 💬`", value="Ver apenas a minha sincera opinião.", inline=False)
    embed.add_field(name="`$curiosidades 🧐`", value="Ver uma curiosidade da FEC.", inline=False)
    embed.add_field(name="`!buscar ou !b 🔎`", value="Buscar um jogador em específico. "
                                                    "Funciona apenas com o zile online ok?", inline=False)
    embed.add_field(name="`$chance🔎`", value="Diz a chance de ganhar ", inline=False)
    embed.add_field(name="`$sorteio 🔎`", value="Sorteia um jogador ou duplas", inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def chance(ctx):
    numero_aleatorio = random.randint(1, 100)
    await ctx.send('A chance é de ' + str(numero_aleatorio) + '%')

@bot.command()
async def sorteio(ctx):
    membros = {
        "membro_zile": "<@558729416067514409>",
        "membro_gabigol": "<@378626663107264513>",
        "membro_minideca": "<@378569893018337300>",
        "membro_vitin": "<@351125755046133760>"
    }

    duplas = [
        [membros["membro_zile"], membros["membro_gabigol"]],
        [membros["membro_minideca"], membros["membro_vitin"]]
    ]

    embed = discord.Embed(title="**Informe o tipo de sorteio (1 - sortear jogador // 2 - sortear dupla) **",
                          color=discord.Color.blue())
    embed.add_field(name="Digite aqui:", value="Aguardando entrada...", inline=False)
    message = await ctx.send(embed=embed)

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        resposta_msg = await bot.wait_for("message", check=check, timeout=60)
    except asyncio.TimeoutError:
        await message.delete()
        await ctx.send("Tempo limite excedido. O sorteio foi cancelado.")
        return

    resposta = resposta_msg.content

    try:
        opcao = int(resposta)
    except ValueError:
        await ctx.send("Opção inválida. O sorteio foi cancelado.")
        return

    if opcao == 1:
        jogador_sorteado = random.choice(list(membros.values()))
        await ctx.send(f"Jogador sorteado: {jogador_sorteado}")
    elif opcao == 2:
        dupla_sorteada = random.choice(duplas)
        dupla_mencionada = " e ".join(dupla_sorteada)
        await ctx.send(f"Dupla sorteada: {dupla_mencionada}")
    else:
        await ctx.send('Opção inválida')

@bot.command()
async def curiosidades(ctx):
    numero_aleatorio = random.randint(1, 25)

    # Obter a menção dos membros desejados usando a sintaxe <@ID_DO_USUÁRIO>
    membro_zile = "<@558729416067514409>"
    membro_gabigol = "<@378626663107264513>"
    membro_minideca = "<@378569893018337300>"
    membro_vitin = "<@351125755046133760>"
    membro_ws = "<@644257150050500658>"

    curiosidades = {

    }

    curiosidade_selecionada = curiosidades.get(numero_aleatorio, "Opção inválida")

    await ctx.send('Momento curiosidade ⁉🔎')
    await ctx.reply(curiosidade_selecionada)
    await ctx.send('Você sabia disso? 🧐')

# Comando opniao
@bot.command()
async def opiniao(ctx):
    numero_aleatorio = random.randint(1, 25)

    # Obter a menção dos membros desejados usando a sintaxe <@ID_DO_USUÁRIO>
    membro_zile = "<@558729416067514409>"
    membro_gabigol = "<@378626663107264513>"
    membro_minideca = "<@378569893018337300>"
    membro_vitin = "<@351125755046133760>"
    membro_ws = "<@644257150050500658>"

    opinioes = {
        
    }

    opniao_selecionada = opinioes.get(numero_aleatorio, "Opção inválida")


    await ctx.reply(opniao_selecionada)
    await ctx.send('Lembre-se, isso é apenas a minha opinião. 🤓')

# Comando Rank Individual
@bot.command()
async def rank_zile(ctx):
    # URL e emoji do jogador Zile
    url_zile = f'https://raw.githubusercontent.com/viniciuszile/Python_Bot/master/Prints/Zile/Zile_{data_atual}.png'
    emoji_zile = '🏆'

    # Obter a referência ao canal de destino
    channel = bot.get_channel(channel_id)

    # Enviar mensagem com a data e o texto do rank
    await channel.send(f'Confira aqui o rank do jogador Zile no dia {data_atual} 📅')
    mensagem = f"Rank do Zile {emoji_zile}"
    await channel.send(mensagem)

    # Baixar a imagem do GitHub
    response = requests.get(url_zile)
    if response.status_code == 200:
        file = discord.File(io.BytesIO(response.content), filename=f'Zile_{data_atual}.png')
        await channel.send(file=file)
    else:
        await channel.send(f'Imagem não encontrada para o jogador Zile na data {data_atual}')


@bot.command()
async def rank_gabigol(ctx):
    # URL e emoji do jogador Gabigol
    url_gabigol = f'https://raw.githubusercontent.com/viniciuszile/Python_Bot/master/Prints/Gabigol/Gabigol_{data_atual}.png'
    emoji_gabigol = '🥇'

    # Obter a referência ao canal de destino
    channel = bot.get_channel(channel_id)

    # Enviar mensagem com a data e o texto do rank
    await channel.send(f'Confira aqui o rank do jogador Gabigol no dia {data_atual} 📅')
    mensagem = f"Rank do Gabigol {emoji_gabigol}"
    await channel.send(mensagem)

    # Baixar a imagem do GitHub
    response = requests.get(url_gabigol)
    if response.status_code == 200:
        file = discord.File(io.BytesIO(response.content), filename=f'Gabigol_{data_atual}.png')
        await channel.send(file=file)
    else:
        await channel.send(f'Imagem não encontrada para o jogador Gabigol na data {data_atual}')


@bot.command()
async def rank_minideca(ctx):
    # URL e emoji do jogador Minideca
    url_minideca = f'https://raw.githubusercontent.com/viniciuszile/Python_Bot/master/Prints/Minideca/Minideca_{data_atual}.png'
    emoji_minideca = '🥈'

    # Obter a referência ao canal de destino
    channel = bot.get_channel(channel_id)

    # Enviar mensagem com a data e o texto do rank
    await channel.send(f'Confira aqui o rank do jogador Minideca no dia {data_atual} 📅')
    mensagem = f"Rank do Minideca {emoji_minideca}"
    await channel.send(mensagem)

    # Baixar a imagem do GitHub
    response = requests.get(url_minideca)
    if response.status_code == 200:
        file = discord.File(io.BytesIO(response.content), filename=f'Minideca_{data_atual}.png')
        await channel.send(file=file)
    else:
        await channel.send(f'Imagem não encontrada para o jogador Minideca na data {data_atual}')


@bot.command()
async def rank_vitin(ctx):
    # URL e emoji do jogador Vitin
    url_vitin = f'https://raw.githubusercontent.com/viniciuszile/Python_Bot/master/Prints/Vitin/Vitin_{data_atual}.png'
    emoji_vitin = '🥉'

    # Obter a referência ao canal de destino
    channel = bot.get_channel(channel_id)

    # Enviar mensagem com a data e o texto do rank
    await channel.send(f'Confira aqui o rank do jogador Vitin no dia {data_atual} 📅')
    mensagem = f"Rank do Vitin {emoji_vitin}"
    await channel.send(mensagem)

    # Baixar a imagem do GitHub
    response = requests.get(url_vitin)
    if response.status_code == 200:
        file = discord.File(io.BytesIO(response.content), filename=f'Vitin_{data_atual}.png')
        await channel.send(file=file)
    else:
        await channel.send(f'Imagem não encontrada para o jogador Vitin na data {data_atual}')

# Comando rank
@bot.command()
async def rank(ctx):

    # Dicionário com os nomes das pastas e seus respectivos arquivos de imagem
    pastas = {
        'Zile': {'url': f'https://raw.githubusercontent.com/viniciuszile/Python_Bot/master/Prints/Zile/Zile_{data_atual}.png',
                 'emoji': '🏆'},
        'Gabigol': {'url': f'https://raw.githubusercontent.com/viniciuszile/Python_Bot/master/Prints/Gabigol/Gabigol_{data_atual}.png',
                    'emoji': '🥇'},
        'Minideca': {'url': f'https://raw.githubusercontent.com/viniciuszile/Python_Bot/master/Prints/Minideca/Minideca_{data_atual}.png',
                     'emoji': '🥈'},
        'Vitin': {'url': f'https://raw.githubusercontent.com/viniciuszile/Python_Bot/master/Prints/Vitin/Vitin_{data_atual}.png',
                  'emoji': '🥉'}
    }

    # Obter a referência ao canal de destino
    channel = bot.get_channel(channel_id)

    # Enviar mensagem com a data e o texto do rank
    await channel.send(f'Confira aqui os ranks do dia {data_atual} 📅')

    # Enviar as fotos de cada pasta
    for pasta, dados in pastas.items():
        mensagem = f"Rank do {pasta} {dados['emoji']}"
        await channel.send(mensagem)

        # Baixar a imagem do GitHub
        response = requests.get(dados['url'])
        if response.status_code == 200:
            file = discord.File(io.BytesIO(response.content), filename=f'{pasta}_{data_atual}.png')
            await channel.send(file=file)
        else:
            await channel.send(f'Imagem não encontrada para {pasta} na data {data_atual}')

        # Pequeno atraso entre o envio de cada foto
        await asyncio.sleep(1)

    print("Todas as imagens foram enviadas com sucesso.")

# Executa o bot
bot.run(token)
