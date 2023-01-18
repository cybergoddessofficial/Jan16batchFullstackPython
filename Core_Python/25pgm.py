lst=[1,2,3,4] #even   :   2+4=6 #odd    :   1+3=4
evensum=0
oddsum=0
for i in lst:
    if(i%2==0):
        evensum=evensum+i
    else:
        oddsum+=i
if(oddsum==0):
    pass
else:
    print(oddsum)
if(evensum==0):
    pass
else:
    print(evensum)