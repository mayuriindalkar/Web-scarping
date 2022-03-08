# from Task_5 import t5
# import pprint
# import os
# from bs4 import BeautifulSoup
# import json
# import requests
# from Task_9 import url_list
# def task13(url_list):
#     if os.path.exists("Task_13.json")==True:
#         with open("Task_12.json","r")as file:
#             data=file.read()
#             t13=json.loads(data)
#         return t13
#     else:
#         final=[]
#         cast_list=[]
#         for k in range(len(url_list)):
#             x=requests.get(url_list[k])
#             soup=BeautifulSoup(x.text,"html.parser")
#             main=soup.find("div",class_="castSection")
#             all=main.find_all("div",class_="cast-item")
#             for i in all:
#                 cast_list.append(i.find("span")["title"])
#             t5[k]["cast"]=cast_list
#             final.append(t5[k])
#             print(final)
#             break
# task13()
	

import requests
from bs4 import BeautifulSoup
from Task_12 import movie_cast
import json

def scrape_movie_details(link):
    cast=(movie_cast(link))
    CastMovieName={}
    url=requests.get(link)
    soup=BeautifulSoup(url.text,"html.parser")
    CastMovieName["movie name"]=soup.find("h1").text
    main=soup.find("div",class_="panel-body content_body")
    InforTable=main.find("ul",class_="content-meta info")
    RowTable=InforTable.find_all("li",class_="meta-row clearfix")
    for i in RowTable:
        CastMovieName[" ".join((i.find("div",class_="meta-label subtle").text).split())]=" ".join((i.find("div",class_="meta-value").text).split())
    CastMovieName["cast"]=cast
    with open("Task_13.json","w") as f:
        json.dump(CastMovieName,f,indent=4)
    return CastMovieName
scrape_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")