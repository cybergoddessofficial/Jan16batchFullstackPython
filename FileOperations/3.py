f=open("a.txt","r")
lst=[]
for lines in f:
    line=lines.rstrip("\n")#string
    word=line.split(" ")#list
    #print(word)
    for i in word:
        lst.append(i)
print(lst)   
for j in lst:
    print(j.upper())     
# Hello All
# Welcome to Python
# ['Hello', 'All']
# ['Welcome', 'to', 'Python']