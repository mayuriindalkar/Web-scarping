from bs4 import BeautifulSoup
import requests
import json
import pprint
import re

def scrap_top_list():
    url1=("https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/")
    sample=requests.get(url1)
    soup=BeautifulSoup(sample.text,"html.parser")
    div=soup.find("table",class_="table")
    main_div=div.find_all("tr")
    movie_ranks=[]
    movie_names=[]
    no_of_Reviews=[]
    movie_urls=[]
    movie_ratings=[]
    year_of_realease=[]



    for i in main_div[1:]:
        movie_rank = i.find("td", class_="bold").text
        movie_ranks.append(movie_rank)
        # print(main_div)
        # print(movie_ranks)
        movie_name = i.find("a", class_="unstyled articleLink").text.strip()
        # print(movie_name)
        name=movie_name
        # print(name)
        movie_name=re.split('(\d+)',name)
        year_of_realease.append(movie_name[-2])
        # print(year_of_realease)

        names=movie_name[0]
        namename=names.replace("(","")
        movie_names.append(namename)
        # print(movie_names)

        movie_review= i.find("td",class_="right hidden-xs").get_text()
        no_of_Reviews.append(movie_review)
        # print(no_of_Reviews)

        movie_rating = i.find("span",class_="tMeterScore").get_text().strip()
        movie_ratings.append(movie_rating)
        # print(movie_rating)

        movie_link=i.find("a")['href']
        movie_urls.append("https://www.rottentomatoes.com"+movie_link)
        # print(movie_urls)


    Top_Movies=[]
    details={'rank':'','Rating':'','Name':'','year':"",'movie_Reviews':'',"movie_urls":""}
    for i in range(0,len(movie_ranks)):
            details['rank']=str(movie_ranks[i])
            details['Rating']=str(movie_ratings[i])
            details['Name']=str(movie_names[i])
            details['year']=str(year_of_realease[i])
            details['movie_Reviews']=str(no_of_Reviews[i])
            details["movie_urls"]=str(movie_urls[i])


            Top_Movies.append(details.copy())

            with open("Task_1.json","w")as file:
                data=json.dump(Top_Movies,file,indent=4)
    return Top_Movies


# pprint.pprint(scrap_top_list())
task1data=scrap_top_list()