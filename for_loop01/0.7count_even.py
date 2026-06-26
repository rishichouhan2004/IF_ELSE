no=int((input("enter the no=",)))
count=0
temp=1
for i in range(len(str(no))):
    if no==0:
        pass
    temp=no%10
    if temp%2==0:
        count=count+1
    no=no//10
print("the count of even no=",count)