import discord
from discord.ext import commands
import sys
import aichat
from google.api_core.exceptions import InternalServerError


intent = discord.Intents.default()
intent.message_content = True

bot = commands.Bot(command_prefix=None, intents=intent)

class muting:
    blockedList = []
    mutedList = []

system = {
    1191137809218687126: "Spider man",
    1191137922427129986: "Doctor Strange",
}

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    msg_author = msg.author
    msg_starts = msg.content.lower().startswith
    sendMsg = msg.channel.send
    server_ID = msg.guild.id
    serverOwner = 720497175368302655
    
    if msg_author.id in muting.mutedList:
        await msg.channel.purge(limit=1)
    else:
        if msg_starts('hello'):
            await sendMsg('Hello!')
        try:
            answer = aichat.module(msg.content, system.get(server_ID))
        except InternalServerError:
            answer = "Yooo yo yo bro. Keep it chill okay. U big man dont use offensive language or IM muting you and thats final"
            muting.blockedList.append(msg_author.id)
            if muting.blockedList.count(msg_author.id) >= 3:
                await sendMsg("that was 3rd time. ur muted")
                muting.mutedList.append(msg_author.id)
        answer = answer[0:-1]
        await sendMsg(answer)
    if msg_author.id == serverOwner:
        if msg_starts("unmute"):
            try:
                user_mention = msg.content.split(' ')[1]
                user_id = int(user_mention[3:-1])
                muting.blockedList.remove(user_id)
                muting.mutedList.remove(user_id)
                await sendMsg("blocked:", muting.mutedList)
            except:
                None
        if msg_starts("delete"):
            try:
                number = msg.content.split(' ')[1]
                await msg.channel.purge(limit=int(number))
            except:
                await sendMsg("what")
        

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    if bot.get_channel(1191137809218687129):
        await bot.get_channel(1191137809218687129).send("im ready bro")

token = "Hide"
bot.run(token)
