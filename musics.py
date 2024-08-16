# musics.py

import requests
from bs4 import BeautifulSoup   



# web-scrapping the billboard website

response =  requests.get("https://www.billboard.com/charts/hot-100/2024-05-12/")

soup = BeautifulSoup(response.text, "html.parser")

musics_divs = soup.find_all(name = "div", class_ = "o-chart-results-list-row-container")

musics = [item.select(selector = "div ul .lrv-u-width-100p ul li h3") for item in musics_divs]

MUSICS = [music[0].string.strip() for music in musics]

print(MUSICS[0])




