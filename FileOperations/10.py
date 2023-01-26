f=open("demo1.txt","r")
for i in f:
    lines=i.rstrip("abcs")  
    print(lines)