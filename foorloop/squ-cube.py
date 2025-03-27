while True:
    print("1.Find the sqaure")
    print("2.Find the cube")
    print("3.Exit")
    # break
    choose=int(input("Choose your number's:(1,2,3)"))
    if choose == 1:
        num=float(input("Enter a number:"))
        print(f"square root of the number is:{num**2}")
        break
    elif choose ==2:
        num=float(input("Enter a number:"))
        print("cube of the number is:",num**3)
        break
    elif choose ==3:
        print("Exited")
        break
    else:
        print("Enter only like (1,2,3) that's it")