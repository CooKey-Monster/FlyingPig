import discord
from bot_settup import bot

class Anime:
	@bot.command()
	async def anime(ctx, _anime: str, _ep: str):
		anime_file = open("anime.txt", "w")
		anime_file.truncate()
		anime_file.write(_anime)
		anime_file.write(_ep)
		anime_file.close()