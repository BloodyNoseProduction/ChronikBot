import requests
from bs4 import BeautifulSoup as bs
import discord
import logging
cFile = open('postList.txt', 'w')
aFile = open('postList.txt', 'a')
url = "https://steemit.com/@chronik-n-coffee"
r = requests.get(url)
soup = bs(r.content, "html.parser")

p_title = soup.find("div", {"class": "articles__summary"})
p_image = soup.find("div", {"class": "articles__content-block--img"})
p_author = soup.find("div", {"class": "author"})

for container in p_title:
    i_title = container.contents[1].text
    print(i_title)
    aFile.write('\n')
    aFile.write(str(i_title))
for item in p_image:
    i_image = item.contents[0].find_all("img")
    print(i_image)
    aFile.write('\n')
    aFile.write(str(i_image))
