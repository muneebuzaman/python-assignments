a=int(input("Enter 1st side:"))
b=int(input("Enger 2nd side:"))
c=int(input("Enter 3rd side:"))
if a>0 and b>0 and c>0:
    if a+b>c and a+c>b and b+c>a:
        print("the triangle is valid.")
    else:
        print("The triangle is not valid.")
else:
    print("All sides must have positive lengths.")