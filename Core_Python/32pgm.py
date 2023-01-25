lst=[1,2,3]
#Nested List
employee=[
    [1,"Nimisha",35000],
    [2,"itheesh",45000],
    [3,"demo",55000]
]
print(employee)
print("the second list:",employee[1])
print(employee[1][1])
s=0

for i in employee:
    print(i)
    print(i[1])
    s+=i[2]
print(s)    

