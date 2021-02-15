import discord
import tenorpy
from bot_settup import bot

class Action:
    @bot.command()
    async def gif(ctx,search):
       embed = discord.Embed(title="Here You Go",colour=discord.Colour.blue())
       t=tenorpy.Tenor()
       gif=t.random(search)
       embed.set_image(url=gif)
       embed.set_footer(text="UwU",icon_url=ctx.author.avatar_url)
       await ctx.send(embed=embed)

    @bot.command()
    async def hug(ctx,user1:discord.Member):
       embed = discord.Embed(title=f"{user1.display_name} Got a Hug From {ctx.author.display_name}",colour=discord.Colour.blue())
       t=tenorpy.Tenor()
       gif=t.random("anime hug")
       embed.set_image(url=gif)
       embed.set_footer(text="UwU",icon_url=ctx.author.avatar_url)
       await ctx.send(embed=embed)

    @bot.command()
    async def slap(ctx,user1:discord.Member):
       embed = discord.Embed(title=f"{user1.display_name} Got a Hug From {ctx.author.display_name}",colour=discord.Colour.blue())
       t=tenorpy.Tenor()
       gif=t.random("anime slap")
       embed.set_image(url=gif)
       embed.set_footer(text="UwU",icon_url=ctx.author.avatar_url)
       await ctx.send(embed=embed)

    @bot.command()
    async def kiss(ctx,user1:discord.Member):
       embed = discord.Embed(title=f"{user1.display_name} Got a Kiss From {ctx.author.display_name}",colour=discord.Colour.blue())
       t=tenorpy.Tenor()
       gif=t.random("anime kiss")
       embed.set_image(url=gif)
       embed.set_footer(text="UwU",icon_url=ctx.author.avatar_url)
       await ctx.send(embed=embed)

    @bot.command()
    async def tickle(ctx,user1:discord.Member):
       embed = discord.Embed(title=f"{user1.display_name} Got Tickled From {ctx.author.display_name}",colour=discord.Colour.blue())
       t=tenorpy.Tenor()
       gif=t.random("anime tickle")
       embed.set_image(url=gif)
       embed.set_footer(text="UwU",icon_url=ctx.author.avatar_url)
       await ctx.send(embed=embed)

    @bot.command()
    async def dance(ctx):
       embed = discord.Embed(title=f"{ctx.author.display_name} Is Dancing",colour=discord.Colour.blue())
       t=tenorpy.Tenor()
       gif=t.random("anime dance")
       embed.set_image(url=gif)
       embed.set_footer(text="UwU",icon_url=ctx.author.avatar_url)
       await ctx.send(embed=embed)

    @bot.command()
    async def cuddle(ctx,user1:discord.Member):
       embed = discord.Embed(title=f"{user1.display_name} Got Cuddled From {ctx.author.display_name}",colour=discord.Colour.blue())
       t=tenorpy.Tenor()
       gif=t.random("anime cuddle")
       embed.set_image(url=gif)
       embed.set_footer(text="UwU",icon_url=ctx.author.avatar_url)
       await ctx.send(embed=embed)

    @bot.command()
    async def blush(ctx):
       embed = discord.Embed(title=f"{ctx.author.display_name} Is Blushing :flush:",colour=discord.Colour.blue())
       t=tenorpy.Tenor()
       gif=t.random("anime blush")
       embed.set_image(url=gif)
       embed.set_footer(text="UwU",icon_url=ctx.author.avatar_url)
       await ctx.send(embed=embed)