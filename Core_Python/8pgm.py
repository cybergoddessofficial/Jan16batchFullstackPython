# i=1
# while(i<=10):#1<=10
#     print(i)#1
#     i+=2

# i=10
# while(i>=1):
#     print(i)
#     i-=1


lower=int(input("enter lower limit:"))#12
upper=int(input("enter upper limit:"))#6
if(lower>=upper):
    print("lower should be smaller")
else:
    while(lower<=upper):
        if(lower%2==0):
            print(lower)
        lower+=1
#1.sum of n numbers b/w two limits
#2.reverse of a number 123 -> 321
#3.sum of cube of digits of number 123 (1**3)+(2**3)+(3**3)
#4.multiplication table of a number