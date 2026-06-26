no=int(input("enter the no="))
digit=int(input(("enter the digit=")))
count=0
temp=0
for i in range(no):
    if i==0:
        pass
    temp=no%10
    if temp==digit:
        count=count+1
    no=no//10
print("the occurence=",count)
