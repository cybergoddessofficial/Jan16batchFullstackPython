f=open("film.txt","r")
dict={}
for lines in f:
    movies=lines.rstrip("\n").split(",")
    # print(movies)
    year=movies[2]
    # print(year)
    if(year not in dict):
        dict[year]=1
    else:
        dict[year]+=1
print("dictionary :",dict)        

lst=[]
for k,v in dict.items():
    lst.append((v,k))
print(lst)
# [(2, '1993'), (3, '2000'), (1, '1998'), (2, '2010')]
sortedlist=sorted(lst,reverse=True)
print(sortedlist)
# [(1, '1998'), (2, '1993'), (2, '2010'), (3, '2000')]
print(sortedlist[0])