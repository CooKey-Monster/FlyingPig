from Sakurajima import Sakurajima

async def download_anime(anime_data):
    client = Sakurajima("ExplosiveDiarrheaPig", "927950", "Z3FsY2QvaFNSYUJXWHErcmhiRDdtZz09")
    my_anime = client.search(anime_data["anime"])[0]
    all_episodes = my_anime.get_episodes()
    episode = all_episodes.get_episode_by_number(anime_data["episode"]) 
    episode.download("fullhd", "anime", "animes")