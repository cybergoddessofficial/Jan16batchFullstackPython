f=open("emp.txt","r")
empid=[]
empname=[]
empage=[]
for lines in f:
    # line=lines.rstrip("\n")
    # value=line.split(",")
    value=lines.rstrip("\n").split(",")
    print(value)
    empid.append(value[0])
    empname.append(value[1])
    empage.append(value[2])
print("id:",empid)
print("name:",empname)
print("Age:",empage)

    