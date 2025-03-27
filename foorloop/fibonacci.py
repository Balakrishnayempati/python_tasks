# num=(int(input("Enter any number:")))
# a,b=0,1
# print("Fabonacci number of:",num)
# for i in range(num):
#   print(a,end=" ")
#   a,b=b,a+b

# num=(int(input("Enter any number")))
# a=0
# b=1
# print("fabonacci number of:",num)
# for i in range(num):
#  print(a,end=" ")
#  a,b=b,a+b
number=(int(input("enter any number:")))
num1=0
num2=1

for i in range(0,number):
    print(num1,end=" ")
    num3=num1+num2
    num1=num2
    num2=num3
