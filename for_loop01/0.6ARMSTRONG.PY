no=int(input("enter the number="))
arm=0
store=1
tem=no
for i in range(len(str(no))):

    store=no%10
    arm=(store**3)+arm
    no=no//10
   
if arm==tem:
    print("armstrome")
else:
    print("not palindrome")


