import discord

client = discord.Client()

colours = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('?resistor'):
        response = '';
        message_trim = message.content.replace('?resistor ', '')
        message_split = message_trim.split()
        if len(message_split) == 1:
            # value -> colours
            value_string = message_split[0].lower()
            if value_string.find('k') != -1:
                # there's a k in there
                value_list = value_string.split('k')
                response = value_list
            else:
                # no k
                response = len(value_string)
        elif len(message_split) == 3:
            # colours -> value
            values = []
            for band in range(3):
                values.append(colours.index(message_split[band]))
            multiplier = 10 ** values[2]
            value = (values[0] * 10 + values[1]) * multiplier
            response = value
        else:
            response = 'Sorry - I don’t understand'
        await message.channel.send(response)

client.run('NzYxNjg2MTE5OTA1MDk5ODQ2.X3eNeg.5Lsf6Hn1lhN1_O4DY_pKY-5YZvw')