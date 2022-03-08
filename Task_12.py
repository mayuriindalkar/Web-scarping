# from bs4 import BeautifulSoup
# import json
# import requests
# import pprint

# def movie_cast(movie_url):
#     list=[]
#     data=requests.get(movie_url)
#     soup=BeautifulSoup(data.text,"html.parser")
#     main=soup.find_all("div",class_="panel-body content_body")
#     # print(main[1])
#     sec=main[1].find("div",class_="castSection")
#     all=sec.find_all("div",class_="cast-item")
#     for i in all:
#         list.append(i.find("span")["title"])
#         # return list

#         with open("Task_12.json","w") as file:
#             json.dump(list,file,indent=4)

#     return list
# pprint.pprint(movie_cast("https://www.rottentomatoes.com/m/black_panther_2018"))


from bs4 import BeautifulSoup
import json
import requests
import pprint
ullist=[]
with open("Task_1.json","r") as file:
    data=file.read()
    last=json.loads(data)
for i in last:
    ullist.append(i["movie_urls"])
def movie_cast(movie_urls):
    dic={}
    for i in movie_urls:
        list=[]
        data=requests.get(i)
        htmlcontent=data.text
        soup=BeautifulSoup(htmlcontent,"html.parser")
        title=soup.find("h1").text
        # main=soup.find_all("div",class_="panel-body content_body")
        # print(main[1])
        list=[]
        sec=soup.find("div",class_="castSection")
        all=sec.find_all("div",class_="cast-item")
        for i in all:
            list.append(i.find("span")["title"])
            # return list
        dic[title]=list

    with open("Task_12.json","w") as file:
        json.dump(list,file,indent=4)
    return list
pprint.pprint(movie_cast(movie_urls=ullist))


