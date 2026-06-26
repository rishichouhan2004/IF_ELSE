a,b=map(int,input("enter the no=").split())
if a<b:
    for i in range(a,b+1):
            print(i,end=" ")
elif a>b:
    for i in range(a,b-1,-1):
        print(i,end=" ")
else:
     print("already on the same floor")