num=(int(input("Enter any number:")))
if num%15==0:
  print(num,"Quess and Buzz")
elif num%3==0:
 print(num,"Quess")
elif num%5==0:
 print(num,"Buzz")
else:
 print(num,"Invalid input")