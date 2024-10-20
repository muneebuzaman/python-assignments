a=int(input("Enter month number:"))
if a== 1 or a== 3 or a== 5 or a== 7 or a== 8 or a== 10 or a== 12:
    print("This month has 31 days.")
elif a == 4 or a == 6 or a == 9 or a == 11:
    print("This month has 30 days.")
elif a==2:
    year = int(input("Enter a year:"))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print( "This month has 29 days.")
            else:
                print("This month has 28 days.")
        else:
            print("This month has 29 days ")
    else:
        print("This month has 28 days")
else:
    print("Invalid month number.")