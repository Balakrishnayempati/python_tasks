num=(int(input("Enter any number:")))
rev=0
while num>0:
    remainder=num%10
    # print(remainder)
    rev=rev*10+remainder
    num=num//10
    # rev+=num
print(rev)