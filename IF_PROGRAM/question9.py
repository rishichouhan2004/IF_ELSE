membership=input("membership is active yes/no=").lower()
books_issued=int(input("enter the book issued="))
if membership=="yes":
    print("entry allowed")
if books_issued<3:
    print("books issued=",books_issued)