lst=[1,2,3,4]
#6(2,4)
element=int(input("enter an element:"))#6
for item in lst: #1,2,3,4
    for i in lst:#1,2,3,4
        s=0
        if(item!=1):
            s=item+i #1+1=2 1+2=3...2+1=3 2+2=4 2+3=5 2+4=6
            if(element==s):#6==2 6==3...6==3 6==4 6==5 6==6
                print(item,i) #2,4
                break
            