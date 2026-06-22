age=int(input("enter the age="))
citizen=input("do you have id=yes/no").lower()
if age>=18:
    if citizen=="yes":
        print("You can vote")
    else:
        print("must be indian")
else:
    print("under age")
