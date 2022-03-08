# from Task_1 import task1data
# import pprint
# import json
# from bs4 import BeautifulSoup
# import requests
# import os                                                                                                   
# import random
# import time


# def get_movie_list_details(movies):
#     if os.path.exists("Task_5.json")==True: 
#         with open("Task_5.json","r") as file:
#             data=file.read()
#             list=json.loads(data)
#         # return list
#     else:
#         time_sleep=random.randint(1,3)
#         j=0
#         list=[]
#         while j<len(movies):
#             newurl=movies[j]["movie_urls"]
#             if os.path.exists(newurl[33:]+".json")==True:
#                 with open (newurl[33:]+".json","r") as file:
#                     data=file.read()
#                     dic=json.loads(data)
#                 list.append(dic)
#             else:
#                 time.sleep(time_sleep)
#                 x=requests.get(newurl)
#             soup=BeautifulSoup(x.text,"html.parser")
#             main=soup.find("ul",class_="content-meta info")
#             all=main.find_all("li",class_="meta-row clearfix")
#             my_dict={}
#             for i in all:
#                 my_dict[i.find("div",class_="meta-label subtle").get_text().strip()]=i.find("div",class_="meta-value").get_text().strip().replace("\n","")
#             title=soup.find("h1")
#             my_dict["name"]=title.text
#             list.append(my_dict)
#             j+=1
#         with open("Task_5.json","w") as file:
#             json.dump(list,file,indent=2)
#         # return list
# # pprint.pprint(get_movie_list_details(task1data))
# get_movie_list_details(task1data[10])

from Task_1 import task1data
import json
import pprint
from bs4 import BeautifulSoup
import requests
i=0
while i<=10:
    def get_movie_details(movies):
        # print(movies)
        j=0
        list4=[]
        while j<len(movies):
            newurl=movies[j]["movie_urls"]
            # print(newurl)
            x=requests.get(newurl)
            soup=BeautifulSoup(x.text,"html.parser")
            movie_find_2=soup.find("ul",class_="content-meta info")
            movie_find_3=movie_find_2.find_all("li",class_="meta-row clearfix")
            my_dict={}
            for i in movie_find_3:
                my_dict[i.find("div",class_="meta-label subtle").text.strip()]=i.find("div",class_="meta-value").text.replace(" ","").replace("\n","").strip()
            list4.append(my_dict)
            j=j+1
        with open("Task_5.json","w") as file:
            json.dump(list4,file,indent=4)
        # pprint.pprint(list4)
        return list4
    # pprint.pprint()
    get_movie_details(task1data) 
i=i+1 