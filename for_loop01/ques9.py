num =  input("Enter number :- ")
count=0
for i in num:
     i= int(i)
     if i%2==0:
            count+=1
if count==len(num):
      print("All numbers are  even")
else:
      print("All numbers are not  even")      
      