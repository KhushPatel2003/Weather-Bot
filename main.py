import discord

#ACTUAL CODE FOR WEATHER
import pyowm 
owm = pyowm.OWM('79a74b9e386227858d196ccc2d008fe4')
city = 'Niagara Falls, CA'
loc = owm.weather_manager().weather_at_place(city)
weather = loc.weather
temp = weather.temperature(unit='celsius')
status = weather.detailed_status
cleaned_temp_data = (int(temp['temp']))
reply1 = "The temperature in " + str(city) + " is " + str(cleaned_temp_data) + u"\u2103"
reply2 = "The day today will have " + str(status) + "."


client = discord.Client()

#@client.event
#async def on_ready():
#    weather_bot_channel = client.get_channel(838887198166220811)
#    await weather_bot_channel.send("test1")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$"):
        await message.channel.send(reply1)
        await message.channel.send(reply2)

client.run('ODM4ODg1NzM1MTg0MDcyNzI0.YJBnOQ.s-Nk2Uzr7bBpbKofot7OW6cufk0')