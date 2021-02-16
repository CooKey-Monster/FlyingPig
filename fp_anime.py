import discord
from bot_settup import bot
from ApiWrapper import Wrapper

class Anime:
    @bot.command()
    async def anime(ctx,*,anime):
        api = Wrapper()
        result = api.search_anime(anime)
        embed = discord.Embed(title = "Anime Results",description = f"Search Results for {anime}",color = discord.Color.green())
        i = 1
        for anime in result:
            embed.add_field(name = f"{i}.", value = f":diamond_shape_with_a_dot_inside: **{anime}**", inline = False)
            i += 1

        await ctx.send(embed = embed, content = ctx.author.mention)