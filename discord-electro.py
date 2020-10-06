import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

colours = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

def colours_to_val(bands):
    values = []
    for band in range(3):
        values.append(colours.index(bands[band]))
    multiplier = 10 ** values[2]
    value = (values[0] * 10 + values[1]) * multiplier
    if value >= 1000000:
        value = value / 1000000
        if value == int(value):
            value = int(value)
        value = str(value) + 'M'
    elif value >= 1000:
        value = value / 1000
        if value == int(value):
            value = int(value)
        value = str(value) + 'k'
    return str(value) + '\u2126'

def val_to_colours(val_list):
    value_string = val_list[0].lower()
    if value_string.find('k') != -1:
        # there's a k in there
        value_list = value_string.split('k')
        value_base = float(value_list[0]) * 1000
        if value_list[1] != '':
            value_base += float(value_list[1]) * 100
    elif value_string.find('m') != -1:
        # there's an m in there
        value_list = value_string.split('m')
        value_base = float(value_list[0]) * 1000000
        if value_list[1] != '':
            value_base += float(value_list[1]) * 100000
        value_string = str(int(value_base))
    bands = []
    bands.append(colours[int(value_string[0:1])])
    bands.append(colours[int(value_string[1:2])])
    bands.append(colours[len(value_string[2:])])
    return '/'.join(bands)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('?r'):
        response = '';
        message_trim = message.content.replace('?r ', '')
        message_split = message_trim.split()
        if len(message_split) == 1:
            try:
                response = val_to_colours(message_split)
            except:
                response = 'I don’t understand. Are you sure that’s a resistance value?'
        elif len(message_split) == 3:
            try:
                response = colours_to_val(message_split)
            except:
                response = 'I don’t understand. I need three colours to tell you the value of the resistor.'
        else:
            response = 'Sorry - I don’t understand. You can either give me a resistance value or  three colours.'
        await message.channel.send(response)

client.run(TOKEN)
