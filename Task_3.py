from Task_1 import scrap_top_list
import json
import pprint

data=scrap_top_list()
def group_by_decade(data):
    dict={}
    list=[]
    for i in data:
        mod=int(i["year"])%10
        decade_year=int(i["year"])-mod
        if decade_year not in list:
            list.append(decade_year)
    # print(list)
    list.sort()
    for i in list:
        movie_list=[]
        for j in data:
            # print(j)
            if int(j["year"])>=i and int(j["year"])<=i+10:
                movie_list.append(j)
                dict[i]=movie_list
    # pprint.pprint(dict)
    with open("Task_3.json","w") as file:
        json.dump(dict,file,indent=4)
group_by_decade(data)