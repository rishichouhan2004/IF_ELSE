number=int(input("enter the number="))
rev=0
tem=number
for i in range(number):
    if number==0:
        break
    rev=rev*10+number%10
    number=number//10
if rev==tem:
    print("palindrome")
else:
    print("not palindrome")
    