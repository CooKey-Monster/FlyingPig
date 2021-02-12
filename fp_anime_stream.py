import discord
from bot_settup import bot
from Sakurajima import Sakurajima

client = Sakurajima("ExplosiveDiarrheaPig", "927950", "Z3FsY2QvaFNSYUJXWHErcmhiRDdtZz09")

def get_anime(anime: str):
    client.search(anime)

class Anime:
    @bot.command()
    async def test(ctx, anime):
        anime_list = get_anime(anime)
        await ctx.send("FLIP THIS WORLD")
    '''@bot.command()
    async def searchanime(ctx, anime):
        print("Started to get the client")
        global client
        print("got the client")
        if client.search(anime) == []:
            print("I don't have results for this anime :(")
            await ctx.send(f"{anime} isn't in my list, try spelling ")
        
        else:
            print("I have results for anime!")
            await ctx.send(f"Here are the results for {anime}:\n{client.search(anime)}")

        print("command done!")


    @bot.command()
    async def playanime(ctx, anime, episode):
        global client
        try:
            my_anime = client.search(anime)[0]
            all_episodes = my_anime.get_episodes()
            episode = all_episodes.get_episode_by_number(episode) 
            episode.download("fullhd", "anime", "C:/Users/baili/OneDrive/Desktop/animes")
        
        except IndexError:
            await ctx.send(f"I don't have episode {episode} of {anime}. Sorry :P")'''