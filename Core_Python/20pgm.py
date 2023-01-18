y=500
def display():
    global y#global declaration
    print(y)
    y="welcome" #modifying value
    print(y)
display()#calling function
print(y)