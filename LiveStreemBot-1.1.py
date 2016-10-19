import discord
import asyncio
import sys
import time
import os
import random

motd = 'Bots!'
motdt = ''
client = discord.Client()
print('Loading...')
token = ""
mode = "0"
tpass = ""


#Settings:
selfbot = True #Changing this to 'False' will break Discords ToS! Use at Your Own Risk. (This Allows other people to use your bot when it is in a user)
motd = 'Bots!'
lmotd = 'Livestreem Time!'
lmotdm = True
#msg:


cmds = ["ls","lsadmin","lscon"]
acmds = ["lsa","lsb","lsc"]
ucmds = ["ls"]
i = '-'
rmdelay = 10
rmd = 10
#getting token from file
if os.path.isdir("config") == False:
    print("Config Folder NOT Found! Creating Dir '/config'")
    os.mkdir("config")
if os.path.exists("config/token.txt") == False:
    print("Token File NOT Found! Creating File 'token.txt'")
    file = open("config/token.txt", "w")
    file.close()
  
file = open("config/token.txt", "r")
token2 = file.read();
file.close()
token3 = token2.split('<%>')
if (str(token3[0]) == "0"):
    token = token3[1]
    mode = "1"
if str(token3[0]) == "1":
    token = token3[1]
    tpass = token3[2]
    mode = "2"
    
if token == "":
    print("Token Empty:")
    input1 = input("Press [1] to Enter Token or [2] To Enter User Account or [3] to exit Bot Program:  ")
    if input1 == "1":
        input2 = input("Enter Token: ")
        filecon = "0" + "<%>" + input2 + "<%>" + "null"
        os.remove("config/token.txt")
        file = open("config/token.txt", "w+")
        file.write(filecon)
        file.close()
        time.sleep(1)
        mode = "1"
        token = input2
        time.sleep(1)
        print("Setup Done!")
        print("Running Bot:")
        time.sleep(1)
        
    elif input1 == "2":
        input2 = input("Enter Email: ")
        input3 = input("Enter Password: ")
        filecon = "1" + "<%>" + input2 + "<%>" + input3
        os.remove("config/token.txt")
        file = open("config/token.txt", "w+")
        file.write(filecon)
        file.close()
        time.sleep(1)
        mode = "2"
        token = input2
        tpass = input3
        time.sleep(1)
        print("Setup Done!")
        print("Running Bot:")
        time.sleep(1)
    else:
        print("Exiting")
        time.sleep(1)
        sys.exit();
else:
    print("USING TOKEN:" + token)
#Folders:
if os.path.isdir("data") == False:
    print("Data Folder NOT Found! Creating Dir '/data'")
    os.mkdir("data")

#Command Reader (Create)
if os.path.exists("config/reader.txt") == False:
    print("Reader File NOT Found! Creating File 'reader.txt'")
    file = open("config/reader.txt", "w")
    file.write("!")
    file.close()
#Command Reader (Get)
file = open("config/reader.txt", "r")
i = file.read();
file.close()
#Admins
if os.path.isdir("data/roles") == False:
    print("roles Folder NOT Found! Creating Dir '/roles'")
    os.mkdir("data/roles")
if os.path.exists("data/roles/admin.txt") == False:
    cmde = ""
    for cmded in cmds:
        cmde = cmde + ";"+cmded
    cmde2 = cmde.replace(";","",1)
    print("AdminList File NOT Found! Creating File 'admin.txt'")
    file = open("data/roles/admin.txt", "w")
    file.write("")
    file.close()
admins = ["test"]
admins.clear()
file = open("data/roles/admin.txt", "r+")
admins = file.read().split(";")
file.close()
#LiveStreem
if os.path.isdir("data/livestream") == False:
    print("livestream Folder NOT Found! Creating Dir '/livestream'")
    os.mkdir("data/livestream")
if os.path.exists("data/livestream/server.txt") == False:
    file = open("data/livestream/server.txt", "w+")
    print("LiveServer File NOT Found! Creating File '/server.txt'")
    file.write("232531062687924224") 
    file.close()
if os.path.exists("data/livestream/mchannel.txt") == False:
    file = open("data/livestream/mchannel.txt", "w+")
    file.write("232531062687924224")
    print("MainChannel File NOT Found! Creating File '/mchannel.txt'")
    file.close()
if os.path.isdir("data/livestream/tmp") == False:
    print("livestreamtmp Folder NOT Found! Creating Dir '/tmp'")
    os.mkdir("data/livestream/tmp")
if os.path.exists("data/livestream/tmp/lchannel.txt") == False:
    file = open("data/livestream/tmp/lchannel.txt", "w+")
    file.write("")
    print("LiveChannel File NOT Found! Creating File '/lchannel.txt'")
    file.close()
#getserver
def getserver(sid):
    for ser in client.servers:
        if (sid == ser.id):
            out = ser
            return out


lserverid = ""
mchannelid = ""
lchannelid = ""
lserver = ""
mchannel = ""
lchannel = ""
lsmode = "0"
lsuser = "Good"
lsurl = "<NotSet>"
file = open("data/livestream/server.txt","r")
lserverid = file.read()
file.close()
file = open("data/livestream/mchannel.txt","r")
mchannelid = file.read()
file.close()
file = open("data/livestream/tmp/lchannel.txt","r")
lchannelid = file.read()
file.close()
if (lchannelid == ""):
    lmode = "0"
#GetServer
def getlmode():
    global lsmode
    return lsmode
def setlmode(mode):
    global lsmode
    lsmode = str(mode)
#rmmsg
async def rmmsg(message,delay):
    msg = message
    de = delay
    await asyncio.sleep(int(de))
    try:
        await client.delete_message(msg)
    except:
        print("ERROR>>Timed Removing Message")

print("Connecting..")
#JoinEvent
@client.event
async def on_ready():
    print("Connection Found")
    await client.change_presence(game=discord.Game(name=motd),status=discord.Status.online)
    #getachannel
    try:
        #lserver = client.get_server(lserverid)
        
        lchannel = client.get_channel(lchannelid)
    
    except:
        print("Somthing Went Wrong Getting Channels. Goodbye!")
        time.sleep(1)
        sys.exit()
    await asyncio.sleep(1)  
    chans = client.get_server(lserverid).channels
    for chn in chans:
        if (chn.name.lower() == "LiveStreem_Chat".lower()):
            await client.delete_channel(chn)  
        
    lserver = getserver(lserverid)
    print("Connected")
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print('')
    print('')
    print('LOG:')
    print('------------------------------')

#CommandEvent
@client.event
async def on_message(msg):
    if (msg.content.startswith(i)):
        men = msg.author.mention + "\n"
       
        args = msg.content.replace(i, '', 1) .split(' ')
        print(msg.content)
        if args[0] in ucmds:
            if args[0] == "emjtest":
                statcon = "*** Bot Status:*** ```"
                statcon = statcon + "\n" + "" + ""
                await client.send_message(msg.channel,men + "This is a test on my Emoji:  " + emj["shd"])
            if args[0] == "ls":
                args.append("")
                args.append("")
                if args[1] == "":
                    rm = await client.send_message(msg.channel,men + "Welcome to ***LIVESTREAM*** **BOT** \n **Commands:** \n ```ls <url,status> - Main LiveStreem Command```")
                    await rmmsg(rm,rmd)
                    await rmmsg(msg,rmd)
                if args[1] == "url":
                    rm = await client.send_message(msg.channel,men + "Livestream URL: " + lsurl)
                    await rmmsg(rm,rmd)
                    await rmmsg(msg,rmd)

                

        if args[0] in acmds:
            if (msg.author.id in admins) == False:
                await client.send_message(msg.channel, men + "Sorry, You can not execute that command")
                return
            if args[0] == "lsa":
                args.append("")
                args.append("")
                args.append("")
                if args[1] == "":
                    await client.send_message(msg.channel, men + "Command Use:" + i + "ls" +  " <start/end/brd/admin>")
                if args[1] == "start":
                    setlmode(1)
                    global lchannelid
                    #everyone = discord.PermissionOverwrite(read_messages=True)
                    #mine = discord.PermissionOverwrite(read_messages=True)
                    #await client.create_channel('Voice', type=discord.ChannelType.voice)
                    lsc = await client.create_channel(getserver(lserverid), 'LiveStreem_Chat')
                    
                    global lchannel
                    lchannel = lsc
                    
                    lchannelid = lsc.id
                    if (lmotdm):
                        await client.change_presence(game=discord.Game(name=lmotd),status=discord.Status.dnd)
                    global lsuser
                    global lsurl
                    comp = lsuser + " LiveStreem" + " | URL: " + lsurl
                    await client.edit_channel(lsc,topic=comp)
                    await client.send_message(lsc, "@here \n  ***LiveStreem Starting!*** \n Channel now **OPEN**! " )
                    await client.send_message(client.get_channel(mchannelid), "@here \n  ***LiveStreem Starting!*** \n Please Go to " + lsc.mention + " Until LiveStreem Ended! " )
                    await asyncio.sleep(60)
                    await client.send_message(client.get_channel(mchannelid), "Info: \n  **4** *mins*  \n Until Channel **Closed** ")
                    await asyncio.sleep(60)
                    await client.send_message(client.get_channel(mchannelid), "Info: \n  **3** *mins*  \n Until Channel **Closed** ")
                    await asyncio.sleep(60)
                    await client.send_message(client.get_channel(mchannelid), "Info: \n  **2** *mins*  \n Until Channel **Closed** ")
                    await asyncio.sleep(60)
                    await client.send_message(client.get_channel(mchannelid), "@here \n  **1** *mins*  \n Until Channel **Closed** ")
                    await asyncio.sleep(30)
                    await client.send_message(client.get_channel(mchannelid), "Info: \n  **30** *secs*  \n Until Channel **Closed** ")
                    await asyncio.sleep(20)
                    await client.send_message(client.get_channel(mchannelid), "Info: \n  **10** *secs*  \n Until Channel **Closed** ")
                    await asyncio.sleep(10)
                    await client.send_message(client.get_channel(mchannelid), "@here \n  **This** Channel  \n is now **CLOSED** ")
                    setlmode(2)
                    await asyncio.sleep(5)
                    await client.send_message(client.get_channel(mchannelid), "@here \n  ***LiveStreem Started!*** \n Please Go to " + lsc.mention + " Until LiveStreem Ended! " )
                    
                    #everyone = discord.PermissionOverwrite(read_messages = False)
                    #await client.edit_channel_permissions(client.get_channel(mchannelid), getserver(lserverid).default_role, everyone)
                if args[1] == "end":
                    setlmode(3)
                    global lchannelid
                    
                    if (lmotdm):
                        await client.change_presence(game=discord.Game(name=motd),status=discord.Status.online)
                    await client.send_message(client.get_channel(mchannelid), "@here \n  ***LiveStreem Ending!*** \n Channel now **OPEN**! " )
                    await client.send_message(client.get_channel(lchannelid), "@here \n  ***LiveStreem Ending!*** \n Please Go back to " + client.get_channel(mchannelid).mention + " Until Next Livestreem! ")
                    await asyncio.sleep(60)
                    await client.send_message(client.get_channel(lchannelid), "Info: \n  **4** *mins*  \n Until Channel **Closed** ")
                    await asyncio.sleep(60)
                    await client.send_message(client.get_channel(lchannelid), "Info: \n  **3** *mins*  \n Until Channel **Closed** ")
                    await asyncio.sleep(60)
                    await client.send_message(client.get_channel(lchannelid), "Info: \n  **2** *mins*  \n Until Channel **Closed** ")
                    await asyncio.sleep(60)
                    await client.send_message(client.get_channel(lchannelid), "Info: \n  **1** *mins*  \n Until Channel **Closed** ")
                    await asyncio.sleep(30)
                    await client.send_message(client.get_channel(lchannelid), "Info: \n  **30** *secs*  \n Until Channel **Closed** ")
                    await asyncio.sleep(20)
                    await client.send_message(client.get_channel(lchannelid), "Info: \n  **10** *secs*  \n Until Channel **Closed** ")
                    await asyncio.sleep(10)
                    await client.send_message(client.get_channel(lchannelid), "@here \n  **this** Channel  \n is now **CLOSED** ")
                    setlmode(4)
                    await asyncio.sleep(5)
                    await client.send_message(client.get_channel(mchannelid), "@here \n  ***LiveStreem Ended!*** \n Please Go to " + client.get_channel(mchannelid).mention + " Until next LiveStreem! " )
                    await asyncio.sleep(60)
                    await client.delete_channel(client.get_channel(lchannelid))
                    setlmode(0)
                if args[1] == "brd":
                    if args[2] == "":
                        rm = await client.send_message(msg.channel, men + "Command Use:" + i + "ls" +  " <brd> <msg>")
                        await rmmsg(rm,rmd)
                        await rmmsg(msg,rmd)
                    else:
                        msgc = msg.content
                        msgcon = msgc
                        msgcon = msgcon.replace("!lsa brd ","",1)
                        await client.send_message(client.get_channel(lchannelid), "@here \n" + msgcon)
                
            if args[0] == "lsb":
                print("lsadmin")
                args.append("")
                args.append("")
                if args[1] == "":
                    rm = await client.send_message(msg.channel,"Command Use:  " + i + "lsadmin <ADD|RM|LIST> <person(Mention)>")
                    rmmsg(rm,30)
                    await rmmsg(msg,rmd)
                if args[1] == "add":
                    if msg.mentions[0].id in admins:
                        rm = await client.send_message(msg.channel,men + " Sorry, That User is **Already** an **ADMIN**")
                        await rmmsg(rm,rmd)
                        await rmmsg(msg,rmd)
                        return
        
                    admins.append(msg.mentions[0].id)
                    filecon = ""
                    for admin in admins:
                        if filecon == "":
                            filecon = filecon + "" + admin
                        else:
                            filecon = filecon + ";" + admin
                    file = open("data/roles/admin.txt", "w")
                    file.truncate()
                    file.write(filecon)
                    file.close()
                    rm = await client.send_message(msg.channel,men + "Added: " + "<@" +msg.mentions[0].id+">" + "   to **Admins**")
                    await rmmsg(rm,rmd)
                    await rmmsg(msg,rmd)
                if args[1] == "rm":
                    if msg.mentions[0].id in admins:
                        admins.remove(msg.mentions[0].id)
                        filecon = ""
                        for admin in admins:
                            if filecon == "":
                                filecon = filecon + "" + admin
                            else:
                                filecon = filecon + ";" + admin
                    
                        file = open("data/roles/admin.txt", "w")
                        file.truncate()
                        file.write(filecon)
                        file.close()
                        rm = await client.send_message(msg.channel,men + "Removed: " + "<@" +msg.mentions[0].id+">" + "   from **Admins**")
                        await rmmsg(rm,rmd)
                        await rmmsg(msg,rmd)
                    else:
                        rm = await client.send_message(msg.channel,men + " Sorry, That User is **not** an **ADMIN**")
                        await rmmsg(rm,rmd)
                        await rmmsg(msg,rmd)
                if args[1] == "list":
                    msgcon = "Admins:"
                    for admin in admins:
                        msgcon = msgcon + "\n" + msg.server.get_member(admin).name
                    rm = await client.send_message(msg.channel,msgcon)
                    await rmmsg(rm,60)
                    await rmmsg(msg,rmd)
            if args[0] == "lsupdat":
                if getlmode() == "0":
                    await client.change_presence(game=discord.Game(name=motd),status=discord.Status.online)
                if getlmode() == "2":
                    await client.change_presence(game=discord.Game(name=motd),status=discord.Status.online)
                    
            if args[0] == "lsc":

                args.append("")
                args.append("")
                args.append("")
                if args[1] == "":
                    await client.send_message(msg.channel,men + i + "lscon" + "<lmotd|motd> <motd>")
                if args[1] == "lmotd":
                    if args[2] == "":
                        rm = await client.send_message(msg.channel,men + i + "lscon" + "<lmotd|motd> <motd>")
                        await rmmsg(rm,rmd)
                        await rmmsg(msg,rmd)
                    else:
                        mocon = msg.content
                        mocon = mocon.replace(i + "lsc lmotd ","",1)
                        global lmotd
                        lmotd = mocon
                        if getlmode() == "2":
                            await client.change_presence(game=discord.Game(name=lmotd),status=discord.Status.dnd)
                        rm = await client.send_message(msg.channel,men + "Set LS-MOTD  to )" +  mocon)
                        await rmmsg(rm,rmd)
                        await rmmsg(msg,rmd)
                if args[1] == "motd":
                    if args[2] == "":
                        await client.send_message(msg.channel,men + i + "ls" + "<lmotd|motd> <motd>")
                    else:
                        mocon = msg.content
                        mocon = mocon.replace(i + "lsc motd ","",1)
                        global motd
                        motd = mocon
                        if getlmode() == "0":
                            await client.change_presence(game=discord.Game(name=mocon),status=discord.Status.online)
                        rm = await client.send_message(msg.channel,men + "Set IDLE - MOTD  to )" +  mocon)
                        await rmmsg(rm,rmd)
                        await rmmsg(msg,rmd)
                if args[1] == "user":
                    if args[2] == "":
                        await client.send_message(msg.channel,men + i + "lsc" + "user <URL>")
                    else:
                        mocon = msg.content
                        mocon = mocon.replace(i + "lsc user ","",1)
                        global lsuser
                        lsuser = mocon
                        if getlmode() == "2" or getlmode() == "1" or getlmode() == "3":
                            global lsurl
                            global lchannelid
                            chtmp = client.get_channel(lchannelid)
                            comp = lsuser + " LiveStreem" + " | URL: " + lsurl
                            print(comp)
                            print(lchannelid)
                            await client.edit_channel(client.get_channel(lchannelid),topic=comp)
                        rm = await client.send_message(msg.channel,men + "Set LS USER  to " +  mocon)
                        await rmmsg(rm,rmd)
                        await rmmsg(msg,rmd)
                if args[1] == "url":
                    if args[2] == "":
                        await client.send_message(msg.channel,men + i + "lsc" + "url <URL>")
                    else:
                        mocon = msg.content
                        mocon = mocon.replace(i + "lsc url ","",1)
                        global lsurl
                        lsurl = mocon
                        if getlmode() == "2" or getlmode() == "1" or getlmode() == "3":
                            global lsuser
                            global lchannelid
                            chtmp = client.get_channel(lchannelid)
                            comp = lsuser + " LiveStreem" + " | URL: " + lsurl
                            print(comp)
                            print(lchannelid)
                            await client.edit_channel(client.get_channel(lchannelid),topic=comp)
                        rm = await client.send_message(msg.channel,men + "Set LS URL  to )" +  mocon)
                        await rmmsg(rm,rmd)
                        await rmmsg(msg,rmd)
                

                    
            if args[0] == "status":
                statcon = "*** Bot Status:*** ```"
                statcon = statcon + "\n" + "" + ""
                
            
    else:
        if msg.channel.id == mchannelid:
            
            if getlmode() == "2":
                if (msg.author.id in admins) == False:
                    await client.send_message(msg.author,"Sorry, This Channel is Closed due to a Livestreem.\n If you wish to talk please head to " + client.get_channel(lchannelid).mention)
                    await client.delete_message(msg)
            if getlmode() == "4":
                if (msg.author.id in admins) == False:
                    await client.send_message(msg.author,"Sorry, This Channel is Closed becuse there is no Livestreem.\n If you wish to talk please head to " + client.get_channel(mchannelid).mention)
                    await client.delete_message(msg)
            


        
try:
    if mode == "1":
        client.run(token)
        print("Connecting..")
    if mode == "2":
        client.run(token,tpass)
        print("Connecting..")
except:
    print("!An Error has Occured While Conecting")
    time.sleep(1)
    sys.exit()

    
