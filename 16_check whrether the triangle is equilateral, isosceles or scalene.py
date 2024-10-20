a=int(input("Enter side a:"))
b=int(input("Enter side b:"))
c=int(input("Enter side c:"))
if a == b and a == c:
    print("It is an equilateral triangle.")
elif a == b or a == c or b == c:
    print("It is an isosceles triangle.")
else:
    print("It is a scalene triangle.")


