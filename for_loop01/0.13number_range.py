a,b=map(int,input("enter the no=").split())
temp=0
if a<b:
    for i in range(a,b+1):
        print(i,end=" ")
elif a>b:
    for i in range(a,b-1,-1):
        print(i,end=" ")
else:
    a==b
    print("both numbers are same")

