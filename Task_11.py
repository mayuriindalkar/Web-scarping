import json 
file=open("Task_5.json","r") 
var=json.load(file)
def get_lang_count(var):
    list1=[]
    list2=[]
    for i in var:
        file1=i["Genre:"].split()
        # print(file1)
        for j in file1:
            if j[-1]==",":
                j=j[:-1]
        list2.append(j)
    for i in list2:
        if i not in list1:
            list1.append(i)
    dict={}
    for l in list1:
        count=0
        h=0
        while h<len(list2):
            if l==list2[h]:
                count+=1
            h+=1
        dict.update({l:count})
    with open("Task_11.json","w") as file:
        json.dump(dict,file,indent=4)
get_lang_count(var)