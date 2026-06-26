number=int(input("enter the number="))
rev=0
for i in range(number):
    if number==0:
        break
    rev=rev*10+number%10
    number=number//10
print("reversed no =",rev)