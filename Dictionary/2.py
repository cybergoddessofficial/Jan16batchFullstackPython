text="hello hi hai hello hi how"
print(text)
words=text.split(" ")
print(words)
dict={}#{"hello":2,"hi":2,"hai":1,"how":1}
for i in words: #'hello', 'hi', 'hai', 'hello', 'hi', 'how'
    if(i not in dict):#hello,hi ,hai,hello
        dict[i]=1 #dict["hello"]=1 | dict["hi"]=1 | dict["hai"]=1
    else:
        dict[i]+=1 #dict["hello"]+=1
print(dict)        