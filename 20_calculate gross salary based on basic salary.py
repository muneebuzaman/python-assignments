bs=int(input("Enter basic salary of an employee:"))
if bs<=10000:
    HRA=(20/100)*bs
    DA=(80/100)*bs
elif bs<=20000:
    HRA=(25/100)*bs
    DA=(90/100)*bs
else:
    HRA=(30/100)*bs
    DA=(95/100)*bs
gross_salary=bs+HRA+DA
print("Gross salary=",gross_salary)

