a=(int(input("Enter a size of the triangle:")))
b=(int(input("Enter b size of the triangle:")))
c=(int(input("Enter c size of the triangle:")))

if a+b>c and a+c>b and b+c>a:
    print("valid triangle")
else:
    print("invalid triangle")