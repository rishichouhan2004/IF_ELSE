username=input("enter the username=").lower()
password=input("enter the password")
if username=="admin":
    print("valid user")
if len(password)>=8:
    print("strong passowrod")