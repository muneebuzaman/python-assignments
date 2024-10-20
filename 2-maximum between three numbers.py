a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if a>b and a>c:
    print(a,"is maximum.")
elif b>c and b>a:
    print(b,"is maximum.")
else:
    print(c,"is maximum.")