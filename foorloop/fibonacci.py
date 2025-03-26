num=(int(input("Enter any number:")))
a,b=0,1
print("Fabonacci number of:",num)
for i in range(num):
  print(a,end=" ")
  a,b=b,a+b