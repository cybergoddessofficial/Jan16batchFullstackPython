# #Binary search
# lst=[10,20,1,2,3,4,5,6]
# print(lst)
# lst.sort()#sort
# print(lst)
# a=len(lst)#length
# print(a)
# print(len(lst))
#

#Linear search
lst=[10,20,1,2,3,4,5]
element=int(input("enter the element:"))#1
for i in lst:#10,20,1,2,3,4,5
    if(element==i): #1==10 1==20 1==1
        flag=1#flag =1
        break
    else:
        flag=0#flag=0
if(flag==1):
    print("elemet found") #print
else:
    print("not found")

