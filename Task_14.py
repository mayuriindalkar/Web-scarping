from multiprocessing.spawn import import_main_path
from bs4 import BeautifulSoup
import json
import requests
from Task_13 import scrape_movie_details
def actor():
    with open("Task_1.json","r") as file:
        data=json.load(file)
    movie_url_list=[]
    for i in data:
        movie_url_list.append(i["movie_urls"])
    list=[]
    for i in range(20):
        list.append(scrape_movie_details(movie_url_list[i]))
    fin_dict={}
    for i in list:
        for j in i["cast"]:
            if j not in fin_dict:
                fin_dict.update({j:[]})
    for i in fin_dict:
        for j in list:
            if i in j["cast"]:
                for k in j["cast"]:
                    if i==k:
                        continue
                    fin_dict[i].append(k)
    with open("Task_14,json","w") as file:
        json.dump(fin_dict,file,indent=4)
actor()