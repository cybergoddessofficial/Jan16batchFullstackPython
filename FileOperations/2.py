f=open("num.txt","r")
lst=[]#empty list
for i in f:
    i=int(i.rstrip("\n"))#string
    print(i)
    lst.append(i)
print(lst)
print("Sum of numbers in file:",sum(lst))
print("largest value:",max(lst))
print("lowest value:",min(lst))