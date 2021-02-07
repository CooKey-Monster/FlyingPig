import json
import random
import discord
from bot_settup import bot
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import has_permissions

account = json.load(open("main_bank.json", "r"))

class Games:
    @bot.command()
    async def rockpaperscissors(ctx):
        global account
        outcomes = {"RP": "win", "RS": "loose", "RR": "draw", "PR": "loose", "PS": "win", "PP": "draw", "SP": "loose", "SR": "win", "SS": "draw"}
        await ctx.send("Let's play rock, paper, scissors!\nType your answer: R, P, or S, I don't cheat(unlike someone...)")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.upper() in ["R", "P", "S"]

        msg = await bot.wait_for("message", check = check)
        robot_choices = random.choice(["R", "P", "S"])
        choices = robot_choices + msg.content
        await ctx.send(robot_choices)

        if outcomes[choices] == "loose":
            await ctx.send(f"You {outcomes[choices]} sucker! I will take 2 coins from u, that's what u get")
            if account[str(ctx.author.id)]["wallet"] >= 2: 
                account[str(ctx.author.id)]["wallet"] -= 2

            else:
                await ctx.send(f"Well, you don't even have 2 coins. Too bad, you get a slap.")

        elif outcomes[choices] == "win":
            await ctx.send(f"You {outcomes[choices]}, congats! Here's 5 coins for you(I put it in your wallet).")
            account[str(ctx.author.id)]["wallet"] += 5

        else:
            await ctx.send(f"It's a {outcomes[choices]}, too bad, you won't get to brag. Here's a coin.")
            account[str(ctx.author.id)]["wallet"] += 1 

        with open("main_bank.json","r") as f:
            account = json.load(f)