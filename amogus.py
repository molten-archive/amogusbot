#!/usr/bin/env python3
import discord, os
from discord.ext import commands
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

bot = commands.Bot(command_prefix=".")
bot.remove_command("help")


@bot.event
async def on_ready():
    print("Imposter is:")
    print(bot.user.name)
    print("------------")


@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
    await user.kick(reason=reason)
    embed = discord.Embed(
        title="Kick",
        description=f"**{user}** has been kicked for **{reason or 'no reason'}**.",
    )
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
    await user.ban(reason=reason)
    embed = discord.Embed(
        title="Ban",
        description=f"**{user}** has been banned for **{reason or 'no reason'}**.",
    )
    await ctx.send(embed=embed)


@bot.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, user: discord.Member, *, reason=None):
    """Mutes person in VC"""
    await user.edit(mute=True)
    embed = discord.Embed(
        title="Mute",
        description=f"**{user}** has been muted for **{reason or 'no reason'}**.",
    )
    await ctx.send(embed=embed)


@bot.command()
async def sus(ctx):
    await ctx.send("sus :flushed:")


@bot.command()
async def amogus(ctx):
    await ctx.send("amogus")


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="Amogus bot", color=0xFF0000)
    embed.add_field(name=".help", value="Displays this command.", inline=False)
    embed.add_field(name=".sus", value="Sus Amogus.", inline=True)
    embed.add_field(name=".amogus", value="Amogus sus.", inline=True)
    embed.add_field(name=".ban", value="Ban a user.", inline=True)
    embed.add_field(name=".kick", value="Kick a user.", inline=True)
    embed.add_field(name=".mute", value="Mute a user.", inline=True)
    await ctx.send(embed=embed)


bot.run(os.getenv("TOKEN"))
