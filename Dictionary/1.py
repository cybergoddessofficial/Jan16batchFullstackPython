# emp={"id":1,"name":"nimisha"}
employee={
    "id":10,
    "name":"Rahul",
    "Designation":"Senior Developer",
    "Salary":36000,
    "Age":100
}
print(employee)
print(employee["name"],employee["Salary"]) #Dictionary_name["key"]
print(employee["Salary"])
#dictionaary_name["key"]="value"
employee["gender"]="Male"
print(employee)
#employee["Salary"]=employee["Salary"]+5000 | 36000+5000
employee["Salary"]+=5000
print(employee["Salary"])
employee["name"]="Nimisha"
print(employee)
print("Salary" in employee)
print("location" in employee)
for i in employee:
    print(i,end=" ")
    print(employee[i])







