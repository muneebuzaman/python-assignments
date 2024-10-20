amount=int(input("Enter amount:"))
note=int(input("Enter note:"))
if note>amount:
   print("note exceeds amount.")
if amount>=500:
    notes=amount//note
    rest=amount%note
    print(notes, "notes of", note, "are present in", amount)
elif amount>=200:
    notes=amount//note
    rest=amount%note
    print(notes, "notes of", note, "are present in", amount)
elif amount>=100:
    notes=amount//note
    rest=amount%note
    print(notes, "notes of", note, "are present in", amount)
elif amount>=50:
    notes=amount//note
    rest=amount%note
    print(notes, "notes of", note, "are present in", amount)
elif amount>=20:
    notes=amount//note
    rest=amount%note
    print(notes, "notes of", note, "are present in", amount)
elif amount>=10:
    notes=amount//note
    rest=amount%note
    print(notes, "notes of", note, "are present in", amount)
else:
    print("amount is less than a note.")


