num1=(int(input("Enter num1 value")))
operater=(input("Enter any operater"))
num2=(int(input("Enter num2 value")))
if operater == "+":
    print(num1+num2)
elif operater == "-":
    print(num1-num2)
elif operater == "*":
    print(num1*num2)
elif operater == "/":
    print(num1/num2)
else:
    print("Enter correct like numbers and opereters(+,-,/,*)")