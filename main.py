import requests
from bs4 import BeautifulSoup

with open('movies_file.txt', 'w') as f:
 URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
 respond=requests.get(URL)
 web=respond.text
 soup=BeautifulSoup(web,"html.parser")
 articles = soup.find_all(name="h3", class_="title")
 rankings=[]
 for rank in articles:
     article_ranking=rank.getText()
     rankings.append(article_ranking+"\n")

 f.writelines(reversed(rankings))
 f.close()
