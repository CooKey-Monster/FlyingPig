from fp_anime import anime_data
from Sakurajima import Sakurajima

def download_anime(anime):
    client = Sakurajima("ExplosiveDiarrheaPig", "927950", "Z3FsY2QvaFNSYUJXWHErcmhiRDdtZz09")
    my_anime = client.search(anime_data["anime"])[0]
    all_episodes = my_anime.get_episodes()
    episode = all_episodes.get_episode_by_number(anime_data["episode"]) 
    episode.download("fullhd", "anime", "C:/Users/baili/OneDrive/Desktop/animes")