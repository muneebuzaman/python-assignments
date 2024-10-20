units=float(input("Enter electricity units:"))
if units>250:
    b=units*1.50
elif units>150 and units<=250:
    b=units*1.20
elif units>50 and units<=150:
    b=units*0.75
else:
    b=units*0.5
surcharge=0.20*b
total_electricity_bill=b+surcharge
print("Total electricity bill= Rs:",total_electricity_bill)
