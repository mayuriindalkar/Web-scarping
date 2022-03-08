import json
import pprint
f=open("Task_13.json","r")
load_data=json.load(f)
f.close()
def analyse_actors(Movie_list):
    list1=[]
    list2=[]
    for movie in Movie_list:
        list1.extend(Movie_list[movie])
    print(list(set(list1)))
    for a in list1:
        final={"Actor":a,"Movies":0}
        for m in Movie_list:
            if a in Movie_list[m]:
                final["Movies"]+=1
        list2.append(final)
    pprint.pprint(list2)
    with open("Task_15.json","w") as file:
        json.dump(list2,file,indent=4)
Task_15=analyse_actors(load_data)

# str2 = "Welcome to my \n Blog"
# print(str2)

# str1 = "Welcome \tto my Blog"
# print(str1)

# str1 = """ Welcome to my 
#                 blog.
#                 This is for
#                 Class X """
# print(str1)

# str="hello"
# print(str[:3])

# a=[1,2,3,4,5,6,7,8,9]
# print(a[1:-5])

# str='MyBLog'                    
# a=' '
# for i in range(len(str)):
#     print(a*str[i])

# for i in range(2,7,2):                
    # print(i * '2')