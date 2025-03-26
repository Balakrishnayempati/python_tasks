n=(int(input("Enter any number:")))
for num in range(0,n+1):  # Numbers from 2 to 50
    for i in range(2, num):  # Check divisibility from 2 to num-1
        if num % i == 0:     # If divisible, it's not prime
            break
    else:
        print(num, end=" ")