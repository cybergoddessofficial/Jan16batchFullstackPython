#factorial of a number
#fact=fact*i
#f=1*2*3*4*5
def fact(n1):
    f=1
    for i in range(1,n1+1):
        f=f*i
    print("Fact is",f)
num=int(input("enter a number:"))
fact(num)