#Binary search
lst=[1,4,2,5,3,6,9]
#ind:0,1,2,3,4,5,6
#--------------------------
#sor:[1,2,3,4,5,6,9]
#ind:0,1,2,3,4,5,6
lst.sort()
print("sorted list:",lst)
flag=0
lower=0 #0
upper=len(lst) #7
print("length of list:",upper)
element=int(input("enter the element:")) #5
while(lower<upper):
    mid=(lower+upper)//2
    if(element>lst[mid]):
        lower=mid+1
    elif(element<lst[mid]):
        upper=mid-1
    elif(element==lst[mid]):
        flag=1
        break
if(flag==1):
    print("element found")    
else:
    print("element not found")    