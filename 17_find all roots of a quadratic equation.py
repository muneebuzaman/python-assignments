a=int(input("Enter cofficient a:"))
b=int(input("Enter cofficient b:"))
c=int(input("Enter cofficient c:"))
D=(b**2)-(4*a*c)
root_1=-b+(D/2*a)**1/2
root_2=-b-(D/2*a)**1/2
if D>0:
    print("Roots are real and distinct")
    print("Roots are",root_1,"and",root_2)
elif D==0:
    print("Roots are real and equal.")
    print("Roots are",root_1,"and",root_2)
else:
    print("No real roots.")


