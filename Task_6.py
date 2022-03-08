import json
def analyse_movies_language():
    file=open("Task_5.json","r")
    var=json.load(file)
    # print(var)
    list=[]
    for i in var:
        if i["Original Language:"] not in list:
            list.append(i["Original Language:"])
            # print(list)
        dict={}
        list1=[]
        for k in list:
            i=0
            count=0
            while i<len(var):
                if k==var[i]["Original Language:"]:
                    count=count+1
                i=i+1
            dict.update({k:count})
        list1.append(dict)
        with open("Task_6.json","w") as file1:
            json.dump(dict,file1,indent=4)
analyse_movies_language()
