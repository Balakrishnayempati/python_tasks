username_data="hello"
userpass_data="123456"
rem_attempts=3
while rem_attempts > 0:
    username_input=input("Enter your username:")
    userpass_input=input("Enter your password:")
    if username_input == username_data and userpass_input == userpass_data:
        print("login successful")
        break
    else:
        rem_attempts-=1
        if rem_attempts ==0:
            print("Sorry you didn't hace access")
        else:
         print("login failed","you still have last",rem_attempts,"attempts")

