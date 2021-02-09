import json
import random
import discord
import fp_games
from bot_settup import bot
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import has_permissions

account = json.load(open("main_bank.json", "r"))

class Economy:
    @bot.command()
    async def bal(ctx, user1: discord.Member = None):
        global account

        if user1 is None:
            wallet = account[str(ctx.author.id)]["wallet"]
            bank = account[str(ctx.author.id)]["bank"]
            embed = discord.Embed(title = f"{ctx.author.display_name} Account Balance", color = discord.Color.green())
            embed.add_field(name = "Wallet", value = f"{wallet} Coins", inline = False)
            embed.add_field(name = "Bank", value = f"{bank} Coins", inline = False)
            embed.add_field(name = "Net value", value = f"{bank + wallet} Coins", inline = False)
            await ctx.send(embed = embed)

        else:
            wallet = account[str(user1.id)]["wallet"]
            bank = account[str(user1.id)]["bank"]
            embed = discord.Embed(title = f"{user1.display_name} Account Balance", color = discord.Color.green())
            embed.add_field(name = "Wallet", value = f"{wallet} Coins", inline = False)
            embed.add_field(name = "Bank", value = f"{bank} Coins", inline = False)
            embed.add_field(name = "Net value", value = f"{bank + wallet} Coins", inline = False)
            await ctx.send(embed = embed)

        fp_games.account = account

    @bot.command()
    @commands.cooldown(3, 30, commands.BucketType.user)
    async def beg(ctx):
        global account
        money = random.randrange(15, 101)
        await ctx.send(f"Sup {ctx.author.mention}, you got {money} coins")

        account[str(ctx.author.id)]["wallet"] += money

        with open("main_bank.json","r+") as f:
            json.dump(account, f, indent = 4)
            f.close()

    @bot.command()
    async def depo(ctx, amount):
        global account
        wallet = account[str(ctx.author.id)]["wallet"]
        bank = account[str(ctx.author.id)]["bank"]

        # check if theirs money, if yes then do the transaction
        if wallet < int(amount):
            await ctx.send(f"Your don't have that much {ctx.author.mention}, get more money to deposit.")

        else:
            account[str(ctx.author.id)]["wallet"] -= int(amount)
            account[str(ctx.author.id)]["bank"] += int(amount)
            await ctx.send(f"Succesfuly deposited {amount} coins into {ctx.author.mention}'s bank. The probability of getting stolen is now even lower.")

            with open("main_bank.json","r+") as f:
                json.dump(account, f, indent = 4)
                f.close()

        # renew wallet then print it
        new_wallet = account[str(ctx.author.id)]["wallet"]
        new_bank = account[str(ctx.author.id)]["bank"]
        embed = discord.Embed(title = f"{ctx.author.display_name} Account Balance", color = discord.Color.green())
        embed.add_field(name = "Wallet", value = f"{new_wallet} Coins", inline = False)
        embed.add_field(name = "Bank", value = f"{new_bank} Coins", inline = False)
        embed.add_field(name = "Net value", value = f"{new_wallet + new_bank} Coins", inline = False)
        await ctx.send(embed = embed)

    @bot.command()
    async def retrieve(ctx, amount):
        global account
        wallet = account[str(ctx.author.id)]["wallet"]
        bank = account[str(ctx.author.id)]["bank"]

        # check if theirs money, if yes then do the transaction
        if bank < int(amount):
            await ctx.send(f"Your don't have that much in your bank {ctx.author.mention}, get more money to retrieve.")

        else:
            account[str(ctx.author.id)]["wallet"] += int(amount)
            account[str(ctx.author.id)]["bank"] -= int(amount)
            await ctx.send(f"Succesfuly retrieved {amount} coins from {ctx.author.mention}'s bank.")

            with open("main_bank.json","r+") as f:
                json.dump(account, f, indent = 4)
                f.close()

        # renew wallet then print it
        new_wallet = account[str(ctx.author.id)]["wallet"]
        new_bank = account[str(ctx.author.id)]["bank"]
        embed = discord.Embed(title = f"{ctx.author.display_name} Account Balance", color = discord.Color.green())
        embed.add_field(name = "Wallet", value = f"{new_wallet} Coins", inline = False)
        embed.add_field(name = "Bank", value = f"{new_bank} Coins", inline = False)
        embed.add_field(name = "Net value", value = f"{new_wallet + new_bank} Coins", inline = False)
        await ctx.send(embed = embed)

    @bot.command()
    async def steal(ctx, user1: discord.Member = None):
        global account

        if user1 is None:
            await ctx.send("You need someone to steal from silly. Or am I just a genius?")

        else:
            await ctx.send(f"target: {user1.mention}")
            amount = random.randint(1, account[str(user1.id)]["wallet"])/2

            if amount - int(amount) != 0:
                amount += 0.5

            else:
                pass

            fee = amount/2
            if fee - int(fee) != 0:
                fee += 0.5

            else:
                pass

            if account[str(user1.id)]["wallet"] > 100 or account[str(user1.id)]["bank"] > 100:
                probability = random.randint(1, 101)

                if probability <= 30:
                    await ctx.send(f"You've stolen {amount} coins from {user1.mention}!")
                    account[str(ctx.author.id)]["wallet"] += amount

                    if account[str(user1.id)]["wallet"] - amount > 0:
                        account[str(user1.id)]["wallet"] -= amount

                    else:
                        account[str(user1.id)]["bank"] -= amount

                else:
                    await ctx.send(f"**WIOUWIOUWIOU!!**\nYour attack failed and {user1.mention} called the police! And that is why you do not steal kids.\n**--{fee}**")
                    
                    if account[str(ctx.author.id)]["wallet"] - amount > 0:
                        account[str(ctx.author.id)]["wallet"] -= amount

                    else:
                        account[str(ctx.author.id)]["bank"] -= amount

            else:
                await ctx.send(f"Can't you see this poor fellow has barely anything!? Shame on you! They'll need these more than you!\n **-{amount} coins**.")
                
                if account[str(ctx.author.id)]["wallet"] - amount > 0:
                    account[str(ctx.author.id)]["wallet"] -= amount

                else:
                    account[str(ctx.author.id)]["bank"] -= amount

            with open("main_bank.json","r+") as f:
                json.dump(account, f, indent = 4)
                f.close()