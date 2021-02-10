import os
import numpy
import discord
from pemdas import calc
from bot_settup import bot
from discord.utils import get
import matplotlib.pyplot as plt
from discord.ext import commands
from discord.ext.commands import has_permissions

class Math:
    @bot.command()
    async def binary(ctx, binary: int):
        await ctx.send(int(binary, 2))

    @bot.command()
    async def hex(ctx, hexadecimal):
        await ctx.send(int(hexadecimal, 16))

    @bot.command()
    async def equation(ctx, expression):
        try:
            await ctx.send(calc(expression))

        except ZeroDivisionError:
            await ctx.send("You cannot divide by zero.\nBecause the inverse of division is multiplication, therefore:\nif a/b = c then a = bc\nbut if 1/0 = c then 1 = 0c, which is false for any number.")

        except ValueError:
            await ctx.send("I can't do algebra yet, so please don't use variables(aka. letters) for pemdas equations, only use them in !fplot")

    @bot.command()
    async def plot(ctx, xpoints, ypoints):
        # plotting the points
        graph_x = xpoints.split(",")
        graph_y = ypoints.split(",")
        x = [int(num) for num in graph_x]
        y = [int(num) for num in graph_y]
        
        plt.plot(x, y)
          
        # naming the x axis 
        plt.xlabel('x - axis') 
        # naming the y axis 
        plt.ylabel('y - axis')
        if ctx.message.author.nick == None:
            plt.title(f'{ctx.message.author.name}\'s Graph')

        else:
            plt.title(f'{ctx.message.author.nick}\'s Graph')

        plt.savefig(fname = 'plot')
        await ctx.send(file = discord.File('plot.png'))
        plt.clf() 

    @bot.command()
    async def fplot(ctx, func, limit1 = -50, limit2 = 50):
        x = []
        y = []
        equation = func

        for i in range(limit1, limit2 + 1):
            x.append(i)
            y.append(calc(equation.replace("x", str(i))))
            equation = func

        plt.plot(x, y)
          
        # naming the x axis 
        plt.xlabel('x - axis') 
        # naming the y axis 
        plt.ylabel('y - axis')
        if ctx.message.author.nick == None:
            plt.title(f'{ctx.message.author.name}\'s Function')

        else:
            plt.title(f'{ctx.message.author.nick}\'s Function')

        plt.savefig(fname = 'function')
        await ctx.send(file = discord.File('function.png'))
        plt.clf()         

    @bot.command()
    async def sin(ctx, number):
        try:
          await ctx.send(f"Sine {number} = {numpy.sin(int(number))}")

        except ValueError:
            await ctx.send(f"{number} isn't a number.")

    @bot.command()
    async def cos(ctx, number):
        try:
            await ctx.send(f"Cosine {number} = {numpy.cos(int(number))}")

        except ValueError:
            await ctx.send(f"{number} isn't a number.")

    @bot.command()
    async def tan(ctx, number):
        try:
            await ctx.send(f"Tangent {number} = {numpy.tan(int(number))}")

        except ValueError:
            await ctx.send(f"{number} isn't a number.")

    @bot.command()
    async def log(ctx, number, base = None):
        if base == None:
            try:
                await ctx.send(f"U did not give an input for a base, I will assume u want the common logarithm, of base 10\nCommon logarithm of {number}: {numpy.log10(int(number))}")

            except ValueError:
                await ctx.send(f"{number} isn't a number.")

        else:
            try:
                await ctx.send(f"Logarithm base {base} of {number} = {numpy.log(int(number)) / numpy.log(int(base))}")

            except ValueError:
                await ctx.send(f"{number} isn't a number.")

    @bot.command()
    async def ln(ctx, number):
        try:
            await ctx.send(f"Natural logarithm of {number}: {numpy.log(int(number))}")

        except ValueError:
            await ctx.send(f"{number} isn't a number.")

    @bot.command()
    async def heron(ctx, side_1, side_2, side_3):
        a = int(side_1)
        b = int(side_2)
        c = int(side_3)
        s = (a + b + c)/2
        poly_1 = s - a
        poly_2 = s - b
        poly_3 = s - c
        if numpy.sqrt(s * poly_1 * poly_2 * poly_3) != 0:
            await ctx.send(f"Area of triangle with sides {a}, {b}, {c} = {numpy.sqrt(s * poly_1 * poly_2 * poly_3)}")

        else:
            await ctx.send(f"It's impossible to have a triangle with sides {a}, {b}, and{c}") 