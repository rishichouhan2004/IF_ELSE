no=int(input("enter the no="))
temp=0
sum=0
for i in range(len(str(no))):
    temp=no%10
    sum=sum+temp

    no=no//10
if sum%2!=0:
    print(" odd")
else:
    print(" even")
       