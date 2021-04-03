#Zennara Bot, a discord bot, by Keagan Landfried, Started December 2018

#import packages
import time
import discord
import os
import asyncio
from keep_alive import keep_alive
from mcstatus import MinecraftServer

client = discord.Client()

version = "1.1.3"

#Discord login successful
@client.event
async def on_ready():
  print("\n-------------")
  print("Logged in as")
  print('   Zennara')
  print("-------------\n")
  print("Version: " + version)
  await client.change_presence(game=discord.Game(name='I-Factions.com | $welcome'))
#toggle alarms
tnewserver = True
tenvoy = False
#envoy alarm
anncID = os.environ.get('anncID')
async def envoy():
  x =203947
  while tenvoy == True:
    clock = int(time.strftime('%X').replace(':', ''))
    if clock == x:
      envmsg  = '@everyone\n\nThe *I-F Envoy Event* is  Starting in **20m**!\nPlease Get Online and Come to **Spawn**!'
      env = await client.send_message(client.get_channel(anncID), envmsg)
      await asyncio.sleep(300)
      await client.delete_message(env)
      envmsg  = '@everyone\n\nThe *I-F Envoy Event* is  Starting in **15m**!\nPlease Get Online and Come to **Spawn**!'
      env = await client.send_message(client.get_channel(anncID), envmsg)
      await asyncio.sleep(300)
      await client.delete_message(env)
      envmsg  = '@everyone\n\nThe *I-F Envoy Event* is  Starting in **10m**!\nPlease Get Online and Come to **Spawn**!'
      env = await client.send_message(client.get_channel(anncID), envmsg)
      await asyncio.sleep(300)
      await client.delete_message(env)
      envmsg  = '@everyone\n\nThe *I-F Envoy Event* is  Starting in **5m**!\nPlease Get Online and Come to **Spawn**!'
      env = await client.send_message(client.get_channel(anncID), envmsg)
      await asyncio.sleep(300)
      await client.delete_message(env)
      start = await client.send_message(client.get_channel(anncID), "@everyone\n\n**The Envoy Has Started! Get on I-F before it is over!**")
      await asyncio.sleep(150)
      await client.delete_message(start)
      end = await client.send_message(client.get_channel(anncID), "The Envoy Event has *Ended*.")
      await asyncio.sleep(600)
      await client.delete_message(end)
    await asyncio.sleep(1)

adminID = os.environ.get('adminID')
#In-Console Discord
async def chat():
  msg = input('>')
  await client.send_message(client.get_channel(adminID), msg)
  await asyncio.sleep(1)

#Autorole
@client.event
async def on_member_join(member):
  role = discord.utils.get(member.server.roles, name='Guest')
  await client.add_roles(member, role)
  joinmsg = "Welcome to the official **SPQR** Botherhood discord server!\nJoin the battle at I-Factions.com !\n***Roma Invicta!***"
  await client.send_message(member, joinmsg)

#on every message
@client.event
async def on_message(message):
  #music commands prompting to user another channel
  #if message.content.startswith(";;") and message.channel.name != "music-commands":
    #await client.send_message(message.channel, "Please use the #)
  #if its a music command (eg. ";;play bitch lasagna")
  if message.content.startswith(";;"):
    return
  #moderation
  x=5
  msg = message.content.lower().replace(" ", "").replace('3', 'e').replace('4', 'a').replace('5', 's').replace('6', 'g').replace('0', 'o').replace('1', 'i')
  while x != 0:
    msg=msg.replace('aa', 'a').replace('bb', 'b').replace('cc', 'c').replace('dd', 'd').replace('ee', 'e').replace('ff', 'f').replace('gg', 'g').replace('hh', 'h').replace('ii', 'i').replace('jj', 'j').replace('kk', 'k').replace('ll', 'l').replace('mm', 'm').replace('nn', 'n').replace('oo', 'o').replace('pp', 'p').replace('qq', 'q').replace('rr', 'r').replace('ss', 's').replace('tt', 't').replace('uu', 'u').replace('vv', 'v').replace('ww', 'w').replace('xx', 'x').replace('yy', 'y').replace('zz', 'z').replace('ck', 'k').replace('tch', 'ch').replace('ir', 'er').replace('ur', 'er')
    x = x-1
  bad = ['niger', 'spik', 'wiger', 'chink', 'retard', 'bich']
  if any(c in msg for c in bad) and "discord admin" not in [y.name.lower() for y in message.author.roles]:
    await asyncio.sleep(0.2)
    await client.delete_message(message)

    await client.send_message(message.author, message.author.mention + ", please do not use blocked words/ terms on the SPQR Discord!")

    await client.send_message(client.get_channel(adminID),message.author.mention + " said the following blacklisted message in " + message.channel.mention + ":\n" + message.content)

  if message.author == client.user:
    return

  #Discord Messages
  tsent = time.strftime('%X %x')
  print(tsent)
  print(message.author, "in", message.channel, "-- ", '"',message.content,'"', "\n")
  print("")

  message.content = message.content.lower()
  #Input Cords
  if message.content.startswith('$newcords'):
    return

  #envoy timer
  if message.content == "$envoy":
    await client.send_message(message.channel, 'The I-F Envoy is at ***5:00PM EST***\n')

  #shows all commands
  if message.content == "$help":
    msg = "`$help`\nShows all commands\n\n`$report (@user) (reason)`\nReports a user to the admins\n\n`$calc ('n-o' or 'o-n') (x-cord) (z-cord)`\nNether/ overworld calculator. 'n-o' is nether to overworld. 'o-n' is overworld to nether\n\n`$welcome`\nWelcome message\n\n`$status`\nShows the status of the mc server\n\n`$login (password)`\nAdministration Login\n\n`$alarm (faction)`\nAlerts all members of a raid.\n\n`$envoy`\nDisplays when the next envoy is.\n\n"
    await client.send_message(message.channel, msg)

  #welcome message
  if message.content == "$welcome":
    msg = "__**IMPORTANT!!**__\n*Thank you for supporting Zennara!*\n\n**Attention:** Please give the Zennara bot administrator permissions or certain moderation commands will not function. However, all other commands will work without administrator.\n\nSend `$help` for a complete list of commands"
    await client.send_message(message.channel, msg)

  #report player to logs channel
  if message.content.startswith("$report") and '@' in message.content[8:]:
    player= message.content
    user = player.split(maxsplit=2)
    msg = "__**New Report**__\n" + "*Accuser-* " + message.author.mention + "\n*Defendent-* " + user[1] + "\n*Reason-* " + ' "' + user[2] + '"'
    await client.send_message(client.get_channel(adminID), msg)#Change ID to your logs channel
    await client.delete_message(message)

  #nether/ overworld calculator
  if message.content.startswith("$calc"):
    cords = message.content
    new = cords.split(maxsplit=3)
    #overworld to nether
    if new[1] == "o-n":
      ntype = "*Overworld to Nether*"
      rx = int(new[2])
      rz = int(new[3])
      x = rx / 8
      z = rz / 8
      nrx = str(x)
      nrz = str(z)
    #nether to overworld
    elif new[1] == "n-o":
      ntype = "*Nether to Overworld*"
      rx = int(new[2])
      rz = int(new[3])
      x = rx * 8
      z = rz * 8
      nrx = str(x)
      nrz = str(z)
    msg = "__**Portal Calculator**__\n**Type:** " + ntype + "\nOld x-val: " + new[2] + "\nOld z-val: " + new[3] + "\n*NEW x-val:* " + nrx + "\n*NEW z-val:* " + nrz
    await client.send_message(message.channel, msg)

  #server info
  if message.content == "$status":
    server = MinecraftServer.lookup('i-factions.com:25565')
    #players and pin
    status = server.status()
    await client.send_message(message.channel, '__**I-NETWORK.IN**__\n*Players=* {0}\n*Ping=* {1}'.format(status.players.online , status.latency))
    
    #Unused, code can display online players
    #query = server.query()
    #print("The server has the following players online: {0}".format(" , ".join(query.players.names)))
  
  #Hidden (not in $help) commands
  if message.content == "$sendnudes":
    await client.send_message(message.channel, "https://www.youtube.com/watch?v=oHg5SJYRHA0")

  if message.content == "$vicarrus" or message.content == "$sibogy":
    await client.send_message(message.channel, 'Vic big dumb')

  if message.content == "$duketedder":
    await client.send_message(message.channel, 'Dkue Mad\nDkue Angry\nDkue **SMASH**')

  if message.content == "$maddles":
    await client.send_message(message.channel, "Maddz Mad")
  
  if message.content == "$randwulf":
    await client.send_message(message.channel, 'DJ Wannwolf')
  
  if message.content == "$xinitiates":
    await client.send_message(message.channel, "Faze 12")

  if message.content == "$Alred":
    await client.send_message(message.channel, 'Alblue')

  #factions commands dont work for people other than faction members
  roles = [y.name.lower() for y in message.author.roles]
  if "discord admin" not in roles or "legionary" not in roles or "centurion" not in roles:
    return
  #Raid Alarm
  if message.content.startswith("$alarm"):

    if message.content == "$alarm":
      msg = '__**RAID ALARM**__\n@everyone\nTriggered by:' +  message.author.mention +'\n\n**All legions online, SPQR is  under seige.**'
      await client.send_message(client.get_channel(anncID), msg)

    #As of now, RQPS is not a faction
    #if message.content == "$alarm rqps":
      #msg = '__**RAID ALARM**__\n@everyon\nTriggered by:' +  message.author.mention +'\n\n**Come online if available! Fellow brethren RQPS is under seige!**'
      #wait client.send_message(client.get_channel(anncID), msg)

    #else: await client.send_message(message.channel, 'Please specify which Sub-Faction is under attack by doing `$alarm spqr` or `$alarm rqps`. If this is a warning, do `$warn`.')

  if message.content == "$warn":
    msg = '__**WARNING**__\n@everyone\nTriggered by:' +  message.author.mention +'\n\n**Attention: An attack on the SPQR Brotherhood is Imminent. Please come online soon.**'
    await client.send_message(client.get_channel(anncID), msg)

  #admin commands dont work for anybody other than admin
  if "discord admin" not in roles:
    return
  #admin log-in
  attempt = message.content[7:]
  password = os.environ.get('password')
  if message.content.startswith('$login'):
    if attempt == password:
      await asyncio.sleep(0.2)
      await client.delete_message(message)
      msg = 'Welcome, Admin ' + message.author.mention + '\n\n*Logs Channel ID*= ' + adminID + '\n\n*Admin Password*= ' + password + '\n\n*Bot Token*= ' + TOKEN + '\n\n*Code Site*= https://repl.it/@KeaganLandfried/Zennara-Bot'
      await client.send_message(client.get_channel(adminID), msg)
    else: 
      await asyncio.sleep(0.2)
      await client.delete_message(message)

  #Mute
  if message.content.startswith("$mute"):
    if message.content[6:] == '@':
      usermute = message.content.split(maxsplit=1)
      if ' ' in usermute[1]:
        usermute = message.content.split(maxsplit=2)
        timemuted = usermute[2].replace('m', '')
      else:
        mutedrole = discord.utils.get(message.server.roles, name='Muted')
        await client.add_roles(usermute[1], mutedrole)
    else:
      await client.send_message(message.channel, "Please *mention* who you want to be muted after the command.")

   #disable envoy and reminder
  if message.conent.startswith("$toggle envoy"):
    if tenvoy == True:
      tenvoy = False
       


#client.loop.create_task(chat())
client.loop.create_task(reminder())
client.loop.create_task(envoy())

keep_alive() #keep the bot running after the window closes, use 
#UptimeRobot to ping the website at least every <60min. to prevent the website from going to sleep, turning off the bot

#make a file named (.env) and write "DISCORD_BOT_SECRET=" with no spaces then paste your discord bot token after it
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
#Admin-logs id
adminID = os.environ.get("adminID")
#run the bot using the token
client.run(TOKEN)