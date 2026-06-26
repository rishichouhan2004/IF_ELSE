no=int(input("enter the no="))
temp=0
mul=1
for i in range(len(str(no))):
    temp=no%10
    mul=mul*temp
    no=no//10
print("the mul=",mul)
if mul%2==0:
    print("even")
else:
    print("odd")
