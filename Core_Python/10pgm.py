num=int(input("enter a number:")) #9
for i in range(2,num): #2,9
    if(num%i==0): #9%2==0 9%3==0 TRUE
        flag=1 #flag=1
        break #break-
    else:
        flag=0 #0
if(flag>0): #TRUE
    print("not prime")
else:
    print("prime number")
