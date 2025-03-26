marks=(int(input("Enter your marks to see your grade:")))
if marks <=100 and marks >=89:
    print(marks,"A grade")
elif marks <70:
    print(marks,"Fail")
elif marks <=89 and marks >=79:
    print(marks,"B grade")
elif marks <=79 and marks>=70:
    print(marks,"C grade")
else:
    print("!invalid enter 1-100")