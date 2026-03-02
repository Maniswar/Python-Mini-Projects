
Small_Pizza  = 100
Medium_Pizza = 200
Large_Pizza  = 300

Pepperoni_For_Small_Pizza  = 30
Pepperoni_For_Medium_Pizza = 40
Pepperoni_For_Large_Pizza  = 50
Cheese_Rs = 20

User   = input("What type of Pizza do you want to Order(S/M/L): ")
Pep    = input("Do you want to add Pepperoni(Y/N): ")
Cheese = input("Do you want to add cheese(Y/N): ")

if User=='S' or User=='s':
    if Pep=='Y' or Pep=='y':
        Bill = Small_Pizza+Pepperoni_For_Small_Pizza
    else:
        Bill=Small_Pizza
elif User=='M' or User=='m':
    if Pep=='Y' or Pep=='y':
        Bill = Medium_Pizza+Pepperoni_For_Medium_Pizza
    else:
        Bill=Medium_Pizza
elif User=='L' or User=='l':
    if Pep=='Y' or Pep=='y':
        Bill = Large_Pizza+Pepperoni_For_Large_Pizza
    else:
        Bill=Large_Pizza
if Cheese=='Y' or Cheese=='y':
    Bill=Bill+Cheese_Rs
    print("Here is your pizza, and the bill is",Bill)
else:
    print("Here is your pizza, and the bill is",Bill)
