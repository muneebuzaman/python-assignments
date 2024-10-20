a=int(input("Enter marks in Mathematics:"))
b=int(input("Enter marks in Physics:"))
c=int(input("Enter marks in Chemistry:"))
d=int(input("Enter marks in Biology:"))
e=int(input("Enter marks in Computer:"))
total_marks=a+b+c+d+e
percentage=(total_marks/500)*100
print("Precentage =",percentage,"%")
if percentage>=90:
    print("and Grade is A")
elif percentage>=80:
    print("and Grade is B")
elif percentage>=70:
    print("and Grade is C")
elif percentage>=60:
    print("and Grade is D")
elif percentage>=40:
    print("and Grade is E")
else:
    print("and Grade is F")
