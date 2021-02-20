import os
import requests
from bs4 import BeautifulSoup

class Wrapper:
	def __init__(self):
		self.search_url = "https://www.youtube.com/results?search_query={}"
		self.headers = {"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"}

	def search_video(self, video_title):
		output = {}
    response = BeautifulSoup(requests.get(self.search_url.format(video_title), headers = self.headers).content, "html.parser")
    container = response.find_all("div", class_="style-scope ytd-item-section-renderer")
    for video in container:
        title_vid = video.find('h3', class_='title')
        href_vid = video.find('h3', class_='href')
        output[str(title_vid)] = str(href_vid) 
    
		for titles in anime_results:
			source_url = [titles.find("a")["href"]]
			for source in source_url:
				output[titles.find("a").contents[0]] = source
		return output
