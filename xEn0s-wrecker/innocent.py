token = "ODA2NjE2MzYxNjM5MDg0MDYz.YJXc4g.8Oi1IMsU23AzUVThw2Y2JFbV00M" # refer to main branch
prefix = "~" 

import discord
from discord.ext import commands
from time import sleep
from tqdm import tqdm
print('\033c')
print("Loading Innocent v3...")
for i in tqdm(range(10)):
    sleep(0.1)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intents, help_command=None, self_bot=True)
# Construct an instance of commands.Bot

@bot.event
async def on_command_error(ctx, error):
    pass

@bot.check
async def command_invoke_delete(ctx):
    try:
        await ctx.message.delete()
    except discord.Forbidden:
        # lol this should never happen
        pass
    finally:
        return True

@bot.event
async def on_ready():
    print('\033c')
    print("""
 ██▓ ███▄    █  ███▄    █  ▒█████   ▄████▄  ▓█████  ███▄    █ ▄▄▄█████▓
▓██▒ ██ ▀█   █  ██ ▀█   █ ▒██▒  ██▒▒██▀ ▀█  ▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒
▒██▒▓██  ▀█ ██▒▓██  ▀█ ██▒▒██░  ██▒▒▓█    ▄ ▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░
░██░▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒██   ██░▒▓▓▄ ▄██▒▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ 
░██░▒██░   ▓██░▒██░   ▓██░░ ████▓▒░▒ ▓███▀ ░░▒████▒▒██░   ▓██░  ▒██▒ ░ 
░▓  ░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ░▒ ▒  ░░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░   
 ▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░  ░ ▒ ▒░   ░  ▒    ░ ░  ░░ ░░   ░ ▒░    ░    
 ▒ ░   ░   ░ ░    ░   ░ ░ ░ ░ ░ ▒  ░           ░      ░   ░ ░   ░      
 ░           ░          ░     ░ ░  ░ ░         ░  ░         ░          
                                   ░



Original Code By: Da532
Modified Splash Screen By: xEn0s


[Bot Prefix]: '~'


[Commands]:
--------------------------------------
[kall] - kicks all members in a server as long as you have permission.

[ball] - bans all members in a server as long as you have permission.

[rall rename_to] - renames every member in the server to the desired rename_to
condition as long as you have permission.

[mall message] - messages every member in a guild with a message of your choice.

[spam x message] - spams message 'x' amount of times in the current channel.
--------------------------------------
""")
print("[INNOCENT V3 IS READY FOR USE.]")

@bot.command()
async def kall(ctx):
    for member in ctx.guild.members:

        if member == bot.user:
            continue

        try:
            await member.kick()
        except discord.Forbidden:
            print(f"{member.name} has FAILED to be kicked from {ctx.guild.name}")
        else:
            print(f"{member.name} has been kicked from {ctx.guild.name}")

    print("Action Completed: kall")

@bot.command()
async def ball(ctx):
    for member in ctx.guild.members:
        
        if member == bot.user:
            continue

        try:
            await member.ban()
        except discord.Forbidden:
            print(f"{member.name} has FAILED to be banned from {ctx.guild.name}")
        else:
            print(f"{member.name} has been kicked from {ctx.guild.name}")
    
    print("Action Completed: ball")  

@bot.command()
async def rall(ctx, *, nick):
    for member in ctx.guild.members:
            
        try:
            await member.edit(nick=nick)
        except discord.Forbidden:
            print(f"{member.name} has NOT been renamed to {nick} in {ctx.guild.name}")
        else:
            print(f"{member.name} has been renamed to {nick} in {ctx.guild.name}")
            
    print("Action Completed: rall")

@bot.command()
async def mall(ctx, *, message):
    for member in ctx.guild.members:
        
        if member == bot.user:
            continue
            
        try:
            await member.send(message)
        except discord.Forbidden:
            print(f"{member.name} has NOT recieved the message.")
        else:
            print(f"{member.name} has recieved the message.")
            
    print("Action Completed: mall")

@bot.command()
async def spam(ctx, amount:int, *, message):
    for member in ctx.guild.members:

        if member == bot.user:
            continue
    for i in range(amount):
        await ctx.send(message)
                
    await all(ctx)

    print("Action Completed: spam")
try:
    bot.run(token, bot=False)
except discord.LoginFailure:
    print('Invalid Token Passed')
