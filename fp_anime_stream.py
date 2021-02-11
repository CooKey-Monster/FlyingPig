import discord
from bot_settup import bot
import chromedriver_binary
from selenium import webdriver

class Anime:
    @bot.command()
    async def test(ctx, path): 
        driver = webdriver.Chrome(path)
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        await ctx.channel.purge(ctx)
        await ctx.send("Done! Hopefully...")