import discord
from bot_settup import bot
from Sakurajima import Sakurajima

client = Sakurajima("ExplosiveDiarrheaPig", "927950", "Z3FsY2QvaFNSYUJXWHErcmhiRDdtZz09")

class Anime:
    @bot.command()
    async def searchanime(ctx, anime: str):
        print("Started to get the client")
        global client
        if client.search(anime) == []:
            print(f"{anime} not found")
        else:
            print(client.search(anime))

    '''@bot.command()
    async def playanime(ctx, anime, episode):
        global client
        try:
            my_anime = client.search(anime)[0]
            all_episodes = my_anime.get_episodes()
            episode = all_episodes.get_episode_by_number(episode) 
            episode.download("fullhd", "anime", "C:/Users/baili/OneDrive/Desktop/animes")
        
        except IndexError:
            await ctx.send(f"I don't have episode {episode} of {anime}. Sorry :P")'''