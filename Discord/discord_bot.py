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
        # curiosidades enviadas pelo zile
        1: f"O {membro_zile} é o único membro da FEC$ capaz de se comunicar com mulheres.",
        2: f"O {membro_gabigol} é o único membro da FEC$ que já ficou drogado sem ter usado droga.",
        3: f"O {membro_minideca} nunca foi amigo da Sara (mesmo indo na casa dela 2 vezes "
           f"e usufruindo da comida, hospitalidade e família dela).",
        4: f"O {membro_vitin}, como forma de flerte, pediu para ser bloqueado no Instagram. "
           f"Você sabia disso? Lembre-se: não julgue as táticas dele, apenas os resultados.",
        5: f"O {membro_ws} aceitou fumar cigarro, para pegar uma mina.",

        # curiosidades enviadas pelo minideca
        6: f"O {membro_zile} é o membro da FEC$ responsável pela saída de outro membro (XxmelokoxX) "
           f"da FEC$.",
        7: f"O {membro_gabigol} apesar de sempre falar que o tempo de vacas magras está chegando, "
           f"saiu comprando passe de jogo que nem joga.",
        8: f"O {membro_minideca} nunca perdeu um clutch 1x1 com a spike plantada.",
        9: f"O {membro_vitin} não consegue falar sem parecer que está chorando.",
        10: f"O {membro_ws} ainda é um membro da FEC$.",

        # curiosidades enviadas pelo vitin
        11: f"O {membro_zile} é o único membro da FEC$ que realizou o ato do coito.",
        12: f"O {membro_gabigol} não pegou uma garota no role e deu a desculpa que estava drogado.",
        13: f"O {membro_minideca} sempre que está jogando de Omen se revela cada vez mais homossexual.",
        14: f"O {membro_vitin}, mesmo depois de levar inúmeros foras, ele continua tentando achar sua player 2, "
            f"mesmo depois de ser bloqueado.",
        15: f"O {membro_ws} é membro da FEC$ junto do {membro_zile} e foram responsáveis pelo Rodrigo "
            f"trancar/reprovar na faculdade.",

        # curiosidades enviadas pelo gabigol
        16: f"O {membro_zile} apesar de namorar, ele é o mais talarico da FEC$.",
        17: f"O {membro_gabigol} tem a incrível habilidade de iludir meninas inocentes no Instagram, "
            f"elas mal sabem que estão se envolvendo com o gabifrouxogol.",
        18: f"O {membro_minideca} apesar de ter um super arsenal de conhecimentos em drogas, ele não as usa, "
            f"em vez disso ele vai trabalhar vendendo camisinha e pesando os outros na farmácia.",
        19: f"O {membro_vitin} é o único membro com o poder de espantar as mulheres. Dizem que ele é até alérgico, "
            f"mas lembre-se, pelo menos ele tenta.",
        20: f"O {membro_ws} é membro da FEC$ e possui vários nomes, entre eles: primo do sagui, ww, ws, ws..ws..ws, "
            f"Bradock, pesão, papai whisky e muito mais.",

        21: f"O {membro_zile} nunca ficou mais de 3 meses em um emprego.",
        22: f"O {membro_gabigol} já teve mais de 17 web's namoros em menos de um mês.",
        23: f"O {membro_minideca} é o único membro da FEC$ que nunca trabalhou.",
        24: f"O {membro_vitin} nunca tirou uma foto com a Ray Ray, apenas o {membro_zile} e o {membro_minideca} "
            f"possuem esse tipo de foto.",
        25: f"O {membro_ws}, quando o {membro_zile} disse que a Sara iria na casa dele, o {membro_ws} sugeriu um trisal? "
            f"(obs: o {membro_zile} nunca nem abraçou a Sara Cristina).",
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
        1: f"O {membro_zile} é o único membro útil da FEC$.",
        2: f"O {membro_gabigol} é o diamante mais fajuto do Valorant.",
        3: f"O {membro_minideca} é o cara mais tóxico da FEC$.",
        4: f"O {membro_vitin} é o cara mais injustiçado da FEC$.",
        5: f"O {membro_ws} é o mais pegador da FEC$.",

        6: f"O {membro_zile} é o membro mais tóxico da FEC$ e todo mundo sabe.",
        7: f"O {membro_gabigol} só sabe jogar com um agente (e quando sabe).",
        8: f"O {membro_minideca} é o melhor (H)omen  da FEC$.",
        9: f"O {membro_vitin} apesar de ter jogado CS:GO, ele é pior que o melokokv no valorant.",
        10: f"O {membro_ws} é o membro mais chavoso da FEC$.",

        11: f"O {membro_zile} é o player mais tóxico/racista/preconceituoso da FEC$.",
        12: f"O {membro_gabigol} gosta de se drogar em roles.",
        13: f"O {membro_minideca} é o cara que mais farpa na FEC$.",
        14: f"O {membro_vitin} é o cara mais injustiçado da FEC$, era para ser platina há muito tempo.",
        15: f"O {membro_ws} é o membro mais caloteiro da FEC$.",

        16: f"O {membro_zile} é o player mais tóxico/machista/xenofóbico da FEC$.",
        17: f"O {membro_gabigol} é sempre julgado pelos seus companheiros de equipe, "
            f"porém chutá-lo todo mundo quer chutar, agora para mamá-lo....",
        18: f"O {membro_minideca} é o cara mais vagabundo da FEC$.",
        19: f"O {membro_vitin} é o pior sova e kj da FEC$ (obs ele é o único).",
        20: f"O {membro_ws} é o membro mais alcoólatra da FEC$.",

        21: f"O {membro_zile} nunca mais foi o mesmo depois da morte do chamer.",
        22: f"O {membro_gabigol} tem apenas dois neurônios, RA-ZE, e mesmo assim eles"
            f" não funcionam direito.",
        23: f"O {membro_minideca} é o main omen menos homem do servidor do Valorant.",
        24: f"O {membro_vitin} tem a maior taxa de HS e o pior rank da FEC$, feito admirável.",
        25: f"O {membro_ws} nunca deveria ter abandonado a fonha, ela realmente o amava.",
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
