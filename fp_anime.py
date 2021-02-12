import discord
from bot_settup import bot

anime_data = {}

class Anime:
	@bot.command()
	async def anime(ctx, _anime: str, _ep: int):
		anime_data["anime"] = _anime
		anime_data["episode"] = _ep