#perform stack operations,push & pop in a list
#perform LIFO in list

size=int(input("enter the size of stack:"))
stk=[] #empty list 4
top=0
print(type(stk))

def push(element):
    global top
    print("PUSH-Insert a value")#4
    if(top>=size):
        print("stack is full")
    else:        
        stk.append(element)
        top+=1
def pop():
    global top
    if(top<=0):
        print("stack is empty")
    else:
        stk.pop()
        top-=1
def display():
    print("elements in stack")
    for i in range(0,top):
        print(stk[i])

n=1
while(n!=0):
    option=int(input("enter operation to perform: 1.push 2.pop 3.display"))
    if(option==1):
        element=int(input("eneter the element:"))
        push(element)
    elif(option==2):
        pop()
    elif(option==3):
        display()
    else:
        print("invalid option...")
    n=int(input("Press 0 to exit | 1 to continue..."))