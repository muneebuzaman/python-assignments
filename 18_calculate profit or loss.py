sp=float(input("Enter selling price:"))
cp=float(input("Enter coast price:"))
profit=sp-cp
loss=cp-sp
if sp>cp:
    print("Rs.",profit,"is profit.")
    profit_per = (profit / cp) * 100
    print("profit percentage=",profit_per)
elif cp>sp:
    print("Rs.",loss,"is loss.")
    loss_per=(loss/cp)*100
    print("loss percentge =",loss_per)
else:
    print("No gain no loss.")
