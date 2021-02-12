import discord
from bot_settup import bot
from Sakurajima import Sakurajima

class Anime:
    @bot.command()
    def searchanime(ctx, anime: str):
        client = Sakurajima("ExplosiveDiarrheaPig", "927950", "Z3FsY2QvaFNSYUJXWHErcmhiRDdtZz09")
        if client.search(anime) == []:
            ctx.send(f"{anime} isn't in my list, try spelling ")

        else:
            ctx.send(f"Here are the results for {anime}:\n{client.search(anime)}")

    @bot.command()
    def playanime(ctx, anime, episode):
        client = Sakurajima("ExplosiveDiarrheaPig", "927950", "Z3FsY2QvaFNSYUJXWHErcmhiRDdtZz09")
        try:
            my_anime = client.search(anime)[0]
            all_episodes = my_anime.get_episodes()
            episode = all_episodes.get_episode_by_number(episode) 
            episode.download("fullhd", "anime", "C:/Users/baili/OneDrive/Desktop/animes")
        
        except IndexError:
            ctx.send(f"I don't have episode {episode} of {anime}. Sorry :P")