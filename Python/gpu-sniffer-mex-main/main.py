import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    modelplus = message.content[8:]
    modelplus = modelplus.replace(" ", "+")
    modelminus = message.content[8:]
    modelminus = modelminus.replace(" ", "-")

    if message.content.startswith('$Buscar '):
        await message.channel.send('Busqueda de '+message.content[8:]+' en existencia:')
        await message.channel.send('https://www.digitalife.com.mx/buscar/t_'+modelminus+'/stock_disponible')
        await message.channel.send('https://dimercom.mx/?swoof=1&product_cat=0&post_type=product&woof_text='+modelplus+'&stock=instock')
        await message.channel.send('https://www.cyberpuerta.mx/index.php?cl=search&searchparam='+modelplus)

client.run(os.getenv('TOKENDISCCORD1'))
