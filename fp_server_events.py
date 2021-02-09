import json
import asyncio
import discord
import requests
from bot_settup import bot
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import has_permissions

account = json.load(open("main_bank.json", "r"))

class Events:
    @bot.event
    async def on_ready():
        global account
        print("Pig is now up and flying")

        game = discord.Game("Flying Pig version 2.5.3")
        await bot.change_presence(status = discord.Status.online, activity = game)

        with open("main_bank.json","r+") as file:
            account = json.load(file)
            file.close()

        while True:
            for members in bot.guilds:
                for member in members.members:
                    if str(member.id) not in account:
                        print("Account Not Exist : Adding Account")
                        account[str(member.id)] = {"wallet" : 0, "bank" : 0}

                    else:
                        print(f"user {str(member.id)} is already registered.")
            
            with open("main_bank.json", "r+") as file:
                json.dump(account, file, indent = 4)
                file.close()
                
            await asyncio.sleep(36000)

    @bot.event
    async def on_member_join(member):
        # Search for channel that has Welcome or welcome, if it does, take id and break
        for channel in member.guild.channels:
            if "welcome" in channel.name or "Welcome" in channel.name:
                welcome_channel_id = channel.id

            else:
                print(channel)

        chl = bot.get_channel(welcome_channel_id)
        embed = discord.Embed(title = f"Welcome {member}", description = "Hope you have a great time", color = discord.Color.blue())
        embed.set_thumbnail(url = member.avatar_url)
        await chl.send(embed = embed)

    @bot.event
    async def on_member_remove(member):
        # Search for channel that has Welcome or welcome, if it does, take id and break
        for channel in member.guild.channels:
            if "bye" in channel.name or "Bye" in channel.name or "farewell" in channel.name or "Farewell" in channel.name:
                bye_channel_id = channel.id

            else:
                print(channel.name)

        chl = bot.get_channel(bye_channel_id)
        embed = discord.Embed(title = f"Good bye {member}", description = "Wish u had a good time :))", color = discord.Color.blue())
        embed.set_thumbnail(url = member.avatar_url)
        await chl.send(embed = embed)

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("**Invalid command. Try using** `help` **to figure out commands!**")

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Please pass in all requirements.**')

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("**You dont have all the requirements or permissions for using this command :angry:**")

        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"**{ctx.author.mention} Stop Begging You Moron. You can use this command 3 Times and the Cooldown Rate is 30 Seconds! Try again in {error.retry_after:.2f}s**")