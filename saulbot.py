# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.ext.commands import has_permissions, MissingPermissions
from discord import Member
import os

description = '''Sup hoe, this is how you navigate my body

All my juicy commands are right down here'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True
intents.messages = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

queues = {}

@bot.event
async def on_ready():
    # await client.change_presence(activity=discord.Game("War Selection"))
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.listen('on_message')
async def lsiten(message):
    words = [ 'kid', 'bebe', 'fetus', 'child', 'little girls', 'the shark', 'juicy k', 'loli', 'lolita', 'baby', 'teen', 'schooler', 'babies', 'infant','toddler', 'rape', 'punish', 'squish', 'molest', 'fertilize', 'gawr', 'gura','shark']

    msg = message.content

    for x in words:
        if x.lower() in msg.lower():
            await message.channel.send(':regional_indicator_j: ')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')       

@bot.command(pass_context = True)
async def join(ctx):
    """Summons my body"""
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
    else:
        await ctx.send("Sit in a channel you idiot")

@bot.command(pass_context = True)
async def leave(ctx):
    """I see how it is, Ungrateful ass...."""
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send('Im out this hoe')
    else:
        await ctx.send('Does it LOOK like im in a channel??')

def check_queue(ctx, id):
    if queues[id] != []:
        voice =ctx.guild.voice_client
        source =queues[id].pop(0)
        player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))

@bot.command(pass_context = True)
async def clear(ctx):
    """Clears the Queue"""
    queues.clear()

@bot.command(pass_context = True)
async def play(ctx, arg):
    """The soundboard"""
    if (ctx.guild.voice_client in  bot.voice_clients) and ctx.voice_client.is_playing(): 
        voice = ctx.guild.voice_client
        song = arg + '.mp3'
        source = FFmpegPCMAudio(song)

        guild_id = ctx.message.guild.id

        if guild_id in queues:
            queues[guild_id].append(source)
            
        else:
            queues[guild_id] = [source]
            
        await ctx.send("Added " + arg +" to queue")

    elif (ctx.guild.voice_client in  bot.voice_clients):
        voice = ctx.guild.voice_client
        song = arg + '.mp3'
        source = FFmpegPCMAudio(song)
        player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))

    elif not ctx.guild.voice_client in bot.voice_clients:
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()

            voice = ctx.guild.voice_client
            song = arg + '.mp3'
            source = FFmpegPCMAudio(song)
            player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))
            playing = True

        else:
            await ctx.send("get in a channel")

def is_connected(ctx):
    voice_client = get(ctx.bot.voice_clients, guild=ctx.guild)
    return voice_client and voice_client.is_connected




@bot.command(pass_context = True)
async def voicelines(ctx):
    """List of voicelines"""
    await ctx.send("benny, david, kevin, kevin2, mevin, montero, peter, peter2, peter3, peter4, sergio, warselection, wide")


@bot.command(pass_context = True)
async def pause(ctx):
    """pauses music"""
    server = ctx.message.guild
    voice_channel = server.voice_client                
    voice_channel.pause()
   

@bot.command(pass_context = True)
async def resume(ctx):
    """Continues paused music"""
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.resume()
    

@bot.command(pass_context = True)
async def skip(ctx):
    """Skips music in the queue"""
    server = ctx.message.guild
    voice_channel = server.voice_client
    voice_channel.stop()
    

@bot.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *,reason=None):
    """Kicks niggas"""
    await member.kick(reason=reason)
    await ctx.send(f'I just kicked that bitch ass nigga {member}')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Who the fuck said you could kick niggas?")

@bot.command(name="mute", pass_context=True)
@has_permissions(manage_roles=True)
async def mute(ctx, member: Member):
    """Mutes niggas"""
    await member.edit(mute=True)

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You can't mute niggas")

@bot.command(name="unmute", pass_context=True)
@has_permissions(manage_roles=True)
async def unmute(ctx, member: Member):
    """Unmutes niggas"""
    await member.edit(mute=False)

@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("No")

@bot.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *,reason=None):
    """Bans niggas"""
    await member.kick(reason=reason)
    await ctx.send(f"You banned {member}? What that nigga do?")

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Squash the beef you ain't banning nobody")

@bot.command(name="vcmute", pass_context=True)
@has_permissions(manage_roles=True)
async def vcmute(ctx):
    """Mutes ALL niggas"""
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=True)

@vcmute.error
async def vcmute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You can't mute niggas")

@bot.command(name="vcunmute", pass_context=True)
@has_permissions(manage_roles=True)
async def vcunmute(ctx):
    """Unmutes ALL niggas"""
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=False)

@vcunmute.error
async def vcunmute_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("No")

@bot.group()
async def juicy(ctx):
    """Is a nigga Juicy?

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'yes, {ctx.subcommand_passed} is juicy as fuck')







bot.run('MTAwNDQwODE0MTI5Njk3NTg5Mw.G492eM.N5igmK8W72yqNAw8aXdgYBOoXSUl8qTcFRtYo8')
