import os
import requests
from bs4 import BeautifulSoup

class Wrapper:
	def __init__(self):
		self.search_url="https://www.animeout.xyz/?s={}"
		self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"}

	def search_anime(self,anime_name):
		output=[]
		response=BeautifulSoup(requests.get(self.search_url.format(anime_name),headers=self.headers).content,"html.parser")
		anime_results=response.find_all("h3",class_="post-title entry-title")
		thumbnails=response.find_all("div",class_="post-image")
		for titles in anime_results:
			source_url=[titles.find("a")["href"]]
			for source in source_url:
				output.append([titles.find("a").contents[0],source])
		return output

	def get_downloads(self,source):
		download_link=[]
		source_response=BeautifulSoup(requests.get(source,headers=self.headers).content,"html.parser")
		source_desc=source_response.find_all("div",class_="article-content")
		for download_links in source_desc:
			downloads=download_links.find_all("a")
			for links in downloads:
				url=links.get("href")
				try:
					if url.endswith(".mkv"):
						download_link.append(url)
				except:
					pass
		return download_link

wrapper = Wrapper()
results = wrapper.search_anime("My hero academia")
print(results)

	# def anime_recommendation(self):
	# 	output=[]
	# 	response=BeautifulSoup(requests.get("https://www.animeout.xyz/download-anime-movies/",headers=self.headers).content,"html.parser")
	# 	movie_list=response.find_all("ul",class_="lcp_catlist")
	# 	for list_index in movie_list:
	# 		for movie in list_index.find_all("li"):
	# 			try:
	# 				output.append(movie.find("a").contents[0])
	# 			except:
	# 				pass
	# 	return output