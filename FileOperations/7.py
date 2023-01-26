f=open("film.txt","r")
dict={}
lst=[]
for lines in f:
    line=lines.rstrip("\n").split(",")
    # print(line)
    rate=line[3]
    movie=line[1]  
    if(movie not in dict):
        dict[movie]=rate
# print(dict)  
for k,v in dict.items():
    print(k,",",v)  

for k,v in dict.items():
    lst.append((v,k))
    lst=sorted(lst,reverse=True)
print(lst)
print(lst[0])
lst=[]
fout=open("covidout4.txt","w")
for i in lst:
    fout.write(str(i))