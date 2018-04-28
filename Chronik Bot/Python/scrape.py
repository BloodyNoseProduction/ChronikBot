import requests
from bs4 import BeautifulSoup as bs
import json
import discord
import logging


url = "https://steemit.com/@chronik-n-coffee"
r = requests.get(url)
soup = bs(r.content, "html.parser")
#aFile = open('postList.txt', 'a')
#cFile = open('postList.txt', 'w')


def steemPostTitle():

    p_title = soup.find("div", {"class": "articles__summary"})

    p_author = soup.find("div", {"class": "author"})

    for container in p_title:
        i_title = container.contents[0].text
        head, sep, tail = i_title.partition('$')
        print(head)
        #aFile.write('\n')
        #aFile.write(str(i_title))
        return head


def steemPostImg():

    p_image = soup.find("div", {"class": "articles__content-block--img"})

    for item in p_image:
        i_image = item.contents[0].find_all("img")[0].get('srcset')
        ihead, isep, itail = i_image.partition('/h')
        print(isep.strip('/') + itail)
        sPi = isep.strip('/') + itail
        #aFile.write('\n')
        #aFile.write(str(isep.strip('/') + itail))
        return sPi

def steemPostDesc():

    p_desc = soup.find("div", {"class": "articles__content-block articles__content-block--text"})

    for container in p_desc:

        i_desc = container.contents[0].text
        head,sep,tail = i_desc.partition("a\U00002026")
        sPd = head.strip("\U00002026") + "\n" + sep

        print(sPd)
        #print(sep)
        #print(tail)
        return sPd

def steemPostLink():
    p_desc = soup.find("div", {"class": "articles__content-block articles__content-block--text"})
    for link in p_desc:
        ilink = link.contents[0].get('href')
        p_link = tuple(set(url) | set(ilink))
        #print(link)
        print('________')
        print(p_link)

steemPostLink()