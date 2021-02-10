import praw
import discord
from bot_settup import bot

reddit = praw.Reddit(
    client_id = "3rQtdVlpAUTQtw",
    client_secret = "zVn5QKI9KrAIbjTJEXi5gyoEJDJvqA",
    user_agent = "my user agent",
    username = "Fabulous_Cricket_863",
    password = "flyingpig"
)

class Reddit:
    @bot.command()
    async def meme(ctx):
        subreddit = reddit.subreddit("memes")
        meme = subreddit.random()
        meme_upvote_percentage = meme.upvote_ratio * 100
        embed = discord.Embed(title = meme.title, color = discord.Color.orange())
        embed.set_image(url = meme.url)
        embed.add_field(name = f"{meme_upvote_percentage}% :arrow_up:", value = "** **", inline = False)
        await ctx.send(embed = embed)

    @bot.command()
    async def funny(ctx):
        subreddit = reddit.subreddit("funny")
        funny = subreddit.random()
        embed = discord.Embed(title = funny.title, color = discord.Color.orange())
        embed.set_image(url = funny.url)
        await ctx.send(embed = embed)

    @bot.command()
    async def quote(ctx):
        subreddit = reddit.subreddit("quotes")
        quote = subreddit.random()
        embed = discord.Embed(title = quote.title, color = discord.Color.orange())
        await ctx.send(embed = embed)