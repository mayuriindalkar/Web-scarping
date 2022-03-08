from Task_1 import scrap_top_list
import json
import pprint

data=scrap_top_list()
def group_by_year(data):
    movies=[]
    for i in data:
        year=i["year"]
        if year not in movies:
            movies.append(year)
    movie_dict={}
    for j in movies:
        movie_list=[]
        for k in data:
            if k["year"]==j:
                movie_list.append(k)
        movie_dict.update({j:movie_list})
        # pprint.pprint(movie_dict)
    # return movie_dict
    with open("Task_2.json","w") as file:
        json.dump(movie_dict,file,indent=4)
group_by_year(data)