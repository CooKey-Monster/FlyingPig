import random
import discord
import requests
import wikipedia
from bot_settup import bot
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import has_permissions

class Commands:
    bot.remove_command("help")

    @bot.command()
    async def spam(ctx, content, number):
        await ctx.channel.purge(limit = 1)
        
        for i in range(int(number)):
            await ctx.send(content)

    @bot.command()
    async def data(ctx, *, content):
        try:
            wiki_page = wikipedia.page(content)
            wiki_summary = wikipedia.summary(content, sentences = 7)
            embed = discord.Embed(title = content, description = wiki_summary, color = discord.Color.red())
            embed.set_image(url = wiki_page.images[0])
            embed.add_field(name = "For more detail, visit the site!", value = wiki_page.url)
            await ctx.send(embed = embed)

        except wikipedia.exceptions.PageError:
            await ctx.send(f"Cannot find {content} on wikipedia, try another subject!")
    
    @bot.command()
    @commands.has_permissions(manage_messages = True)
    async def clear(ctx, amount):
        try:
            amount = int(amount) + 1
            await ctx.channel.purge(limit = amount)
            msg = await ctx.send(f"**{amount} Message Cleared by {ctx.author.mention}!**")
            await msg.delete(delay = 3)
            
        except ValueError:
            await ctx.send(f"{number} is not a number, you cannot clear {number - 1} message(s)")

    @bot.command()
    async def info(ctx, user1: discord.Member = None):
        if user1 is None:
            roles = [role for role in ctx.author.roles]
            embed = discord.Embed(color = discord.Color.blue())
            embed.add_field(name = "Account Created", value = f"".join(ctx.author.created_at.strftime("%A, %B %d %Y, %H:%M:%S %p")))
            embed.add_field(name = "Server Joined", value = f"".join(ctx.author.joined_at.strftime("%A, %B %d %Y, %H:%M:%S %p")))
            embed.add_field(name = "Roles", value = "    ".join([role.mention for role in roles]), inline = False)
            embed.add_field(name = "Highest Roles", value = f"{ctx.author.top_role.mention}")
            embed.set_footer(text = f"Account ID : {ctx.author.id}")
            embed.set_thumbnail(url = ctx.author.avatar_url)
            embed.set_author(name = f"{ctx.author}", icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)

        else:
            roles = [role for role in user1.roles]
            embed = discord.Embed(color = discord.Color.blue())
            embed.add_field(name = "Account Created", value = f"".join(user1.created_at.strftime("%A, %B %d %Y, %H:%M:%S %p")))
            embed.add_field(name = "Server Joined", value = f"".join(user1.joined_at.strftime("%A, %B %d %Y, %H:%M:%S %p")))
            embed.add_field(name = "Roles", value = "    ".join([role.mention for role in roles]), inline = False)
            embed.add_field(name = "Highest Roles", value = f"{user1.top_role.mention}")
            embed.set_footer(text = f"Account ID : {user1.id}")
            embed.set_thumbnail(url = user1.avatar_url)
            embed.set_author(name = f"{user1}", icon_url = user1.avatar_url)
            await ctx.send(embed = embed)          

    @bot.command()
    async def pfp(ctx, user1: discord.Member = None):
        if user1 is None:
            useravatar = ctx.author.avatar_url_as(static_format = 'png', size = 4096)
            embed = discord.Embed(title = f"{ctx.author.display_name} Profile Picture", color = discord.Color.green())
            embed.set_image(url = useravatar)
            await ctx.send(embed = embed)

        else:
            useravatar = user1.avatar_url_as(static_format = 'png', size = 4096)
            embed = discord.Embed(title = f"{user1.display_name} Profile Picture", color = discord.Color.green())
            embed.set_image(url = useravatar)
            await ctx.send(embed = embed)

    @bot.command()
    async def membercount(ctx):
        server_id = bot.get_guild(ctx.guild.id)
        server_member_count = server_id.member_count
        embed = discord.Embed(title = f"members in {ctx.guild.name}", description = server_member_count, color = discord.Color.purple())
        await ctx.send(embed = embed)

    @bot.command()
    async def news(ctx):
        main_url = ('http://newsapi.org/v2/top-headlines?'
                    'country=us&'
                    'apiKey=08328b13a08a4f5694c108a103060df2')

        open_bbc_page = requests.get(main_url).json() 

        # getting all articles in a string article 
        article = open_bbc_page["articles"]
        results = []
        des = []
        content = []
        urls = []

        for ar in article: 
            results.append(ar["title"]) 
            des.append(ar["description"])
            content.append(ar["content"])
            urls.append(ar["url"])

        embed = discord.Embed(title = results[0], description = "{}\n Link : {}".format(content[0], urls[0]), color = discord.Color.red())
        embed.add_field(name = results[1], value = "{}\n Link : {}".format(content[1], urls[1]), inline = False)
        embed.add_field(name = results[2], value = "{}\n Link : {}".format(content[2], urls[2]), inline = False)
        embed.add_field(name = results[3], value = "{}\n Link : {}".format(content[3], urls[3]), inline = False)
        embed.add_field(name = results[4], value = "{}\n Link : {}".format(content[4], urls[4]), inline = False)
        embed.add_field(name = results[5], value = "{}\n Link : {}".format(content[5], urls[5]), inline = False)
        embed.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Google_News_Logo.svg/1200px-Google_News_Logo.svg.png")
        await ctx.send(embed = embed)

    @bot.command()
    @commands.has_permissions(manage_permissions = True)
    async def mute(ctx,user1:discord.Member,*,args = None):
        mute = discord.utils.get(ctx.guild.roles,name = 'Muted')
        role = discord.utils.find(lambda r: r.name == 'Muted', ctx.guild.roles)
        if role in user1.roles:
            embed = discord.Embed(title = f"You Can't Mute Someone Who Is Already Muted!",color = discord.Color.green())
            embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/799678768066592799/6d72d4bc4fdd9f21935769c2fd7a0d46.png?size=4096")
            await ctx.send(embed = embed)

        else:
            if args:
                await user1.add_roles(mute)
                embed = discord.Embed(title = f"{user1} Has Been Muted!",description = f"Reason : {args}",color = discord.Color.green())
                embed.set_image(url = "https://i0.wp.com/themarvelreport.com/wp-content/uploads/2018/04/Gzx1YXS.gif")
                embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/799678768066592799/6d72d4bc4fdd9f21935769c2fd7a0d46.png?size=4096")
                await ctx.send(embed = embed)

            else:
                await user1.add_roles(mute)
                embed = discord.Embed(title = f"{user1} Has Been Muted!",description = f"Reason : {args}",color = discord.Color.green())
                embed.set_image(url = "https://i0.wp.com/themarvelreport.com/wp-content/uploads/2018/04/Gzx1YXS.gif")
                embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/799678768066592799/6d72d4bc4fdd9f21935769c2fd7a0d46.png?size=4096")
                await ctx.send(embed = embed)

    @bot.command()
    @commands.has_permissions(manage_permissions = True)
    async def unmute(ctx,user1:discord.Member):

        unmute = discord.utils.get(ctx.guild.roles,name = 'Muted')
        role = discord.utils.find(lambda r: r.name == 'Muted', ctx.guild.roles)

        if role in user1.roles:
            await user1.remove_roles(unmute)
            embed = discord.Embed(title = f"{user1} Is Unmuted!", description = "WE ARE IN THE ENDGAME NOW",color = discord.Color.green())
            embed.set_image(url = "https://economicsandethics.typepad.com/.a/6a0120a58aead7970c0240a4816058200d-800wi")
            embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/799678768066592799/6d72d4bc4fdd9f21935769c2fd7a0d46.png?size=4096")
            await ctx.send(embed = embed)
        
        elif role not in user1.roles:
            embed = discord.Embed(title = f"You Can't Unmute Someone Who Is Not Muted!",color = discord.Color.green())
            embed.set_image(url = "https://i0.wp.com/themarvelreport.com/wp-content/uploads/2018/04/Gzx1YXS.gif")
            embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/799678768066592799/6d72d4bc4fdd9f21935769c2fd7a0d46.png?size=4096")
            await ctx.send(embed = embed)

    @bot.command()
    async def report(ctx, user:discord.Member, *, info):
        await ctx.message.delete()
        await ctx.send(f"**{ctx.author.mention} Thank You For Reporting. Any Online Staff/Mods/Admin Will Check That And Take Actions! Thank You.**")
        embed = discord.Embed(title = f"{ctx.author.display_name} Just Reported {user}", description = f"Reason : {info}", color = discord.Color.red())
        for channel in ctx.guild.channels:
            if "report" in channel.name or "mod-mail" in channel.name:
                report_channel = channel

            else:
                print(channel)

        await report_channel.send(embed = embed)

    @bot.command()
    async def invite(ctx):
        link = "https://discord.com/api/oauth2/authorize?client_id=799678768066592799&permissions=0&scope=bot"
        embed = discord.Embed(title = "Invite Link", description = "You can invite me to your server by just clicking on the link.", color = discord.Color.purple())
        embed.add_field(name = "Link", value = link, inline = False)
        embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/799678768066592799/6d72d4bc4fdd9f21935769c2fd7a0d46.png?size=4096")
        await ctx.send(embed = embed)

    @bot.command()
    async def help(ctx):
        embed = discord.Embed(title = "Help on FlyingPig.", description = "My commands")
        embed.add_field(name = "!help", value = "Shows this.", inline = False)
        embed.add_field(name = "!report @user **some reason**", value = "Report user for reason", inline = False)
        embed.add_field(name = "!invite", value = "Invite link for FLyingPig.", inline = False)
        embed.add_field(name = "!mute @user", value = "Mute user.", inline = False)
        embed.add_field(name = "!unmute @user", value = "Unmute user.", inline = False)
        embed.add_field(name = "!data subject", value = "Shows wiki info about subject.", inline = False)
        embed.add_field(name = "!pfp @user", value = "Prints the user's pfp in the channel, but bigger.", inline = False)
        embed.add_field(name = "!clear #number", value = "Clear messages #number times, must be admin.", inline = False)
        embed.add_field(name = "!info @user", value = "Gives info about the user", inline = False)
        embed.add_field(name = "!membercount", value = "Display number of members.", inline = False)
        embed.add_field(name = "!news", value = "Shows latest news.", inline = False)
        embed.add_field(name = "!RedditHelp", value = "Shows Reddit commands.", inline = False)
        embed.add_field(name = "!GameHelp", value = "Shows games.", inline = False)
        embed.add_field(name = "!MoneyHelp", value = "Shows economy commands.", inline = False)
        embed.add_field(name = "!MathHelp", value = "Shows math commands.", inline = False)
        embed.add_field(name = "!ActionHelp", value = "Shows actions.", inline = False)
        await ctx.send(embed = embed)

    @bot.command()
    async def RedditHelp(ctx):
        embed = discord.Embed(title = "Help on Reddit commands on FlyingPig.", description = "My Reddit commands")
        embed.add_field(name = "!meme", value = "Shows you a random meme.", inline = False)
        embed.add_field(name = "!funny", value = "Shows you a funny pic/topic.", inline = False)
        embed.add_field(name = "!quote", value = "Shows you an inspirational quote/saying.", inline = False)        
        await ctx.send(embed = embed)

    @bot.command()
    async def GameHelp(ctx):
        embed = discord.Embed(title = "Help on games commands on FlyingPig.", description = "My game commands")
        embed.add_field(name = "!rockpaperscissors", value = "Play rock, paper, scissors shoot!", inline = False)
        await ctx.send(embed = embed)

    @bot.command()
    async def MoneyHelp(ctx):
        embed = discord.Embed(title = "Help on economy commands on FlyingPig.", description = "My economy commands")
        embed.add_field(name = "!bal @user", value = "Shows balance of @user, default is self.", inline = False)
        embed.add_field(name = "!beg", value = "Beg the majestic pig to give u some coins, goes directly to your wallet.", inline = False)
        embed.add_field(name = "!retrieve #amount", value = "Retrieve #amount from bank, to wallet.", inline = False)
        embed.add_field(name = "!depo #amount", value = "Deposits #amount into bank.", inline = False)  
        embed.add_field(name = "!steal @user", value = "Steal money from @user", inline = False)
        embed.add_field(name = "!gift #amount @user", value = "You give #amount coins to @user, money comes from your wallet/bank.", inline = False)               
        await ctx.send(embed = embed)

    @bot.command()
    async def MathHelp(ctx):
        embed = discord.Embed(title = "Help on math commands on FlyingPig.", description = "My math commands")
        embed.add_field(name = "!hex #hexadecimal", value = "Convert hexadecimal into decimal", inline = False)
        embed.add_field(name = "!binary #binary", value = "Convert binary into decimal", inline = False)
        embed.add_field(name = "!fplot function", value = "Plots function", inline = False)
        embed.add_field(name = "!plot xpoints ypoints", value = "Plots points at xpoints and ypoints(every xpoints and ypoints must be seperated with a comma, and all xpoints and ypoints most be surrounded by double quotes). The first xpoints matches the first ypoints.", inline = False)
        embed.add_field(name = "!equation equation", value = "Finds answer to equation, syntax is the same as you would use on google.", inline = False)
        embed.add_field(name = "!log #number #base", value = "Finds log, by default, base 10, of #number.", inline = False)
        embed.add_field(name = "!ln #number", value = "Finds natural logarithm, base e, of #number", inline = False)
        embed.add_field(name = "!sin #number", value = "Finds sine value of #number(trigonometry)", inline = False)
        embed.add_field(name = "!cos #number", value = "Finds cosine value of #number(trigonometry)", inline = False)
        embed.add_field(name = "!tan #number", value = "Finds tangent value of #number(trigonometry)", inline = False)        
        embed.add_field(name = "!heron #side1 #side2 #side3", value = "Finds area of a triangle with sides: #side1 #side2 #side3. If it's 0, then such triangles does not exist.", inline = False)
        await ctx.send(embed = embed)

    @bot.command()
    async def ActionHelp(ctx):
        embed = discord.Embed(title = "Help on action commands on FlyingPig.", description = "My actions")
        embed.add_field(name = "!gif object", value = "Search object in gif", inline = False)
        embed.add_field(name = "!hug @user", value = "Use .hug @user", inline = False)
        embed.add_field(name = "!kiss @user", value = "Use .kiss @user", inline = False)
        embed.add_field(name = "!cuddle @user", value = "Use .cuddle @user", inline = False)
        embed.add_field(name = "!blush @user", value = "Use .blush", inline = False)
        embed.add_field(name = "!tickle @user", value = "Use .tickle @user", inline = False)
        embed.add_field(name = "!slap @user", value = "Use .slap @user", inline = False)
        embed.add_field(name = "!dance", value = "Use .dance",inline = False)