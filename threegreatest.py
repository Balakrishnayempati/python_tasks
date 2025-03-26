n1=(int(input("Enter any number")))
n2=(int(input("Enter any number")))
n3=(int(input("Enter any number")))

if n1>=n2 and n1>=n3:
    print(n1,"Bigger")
elif n2>=n1 and n2>=n3:
    print(n2,"Bigger")
else:
    print(n3,"Bigger")