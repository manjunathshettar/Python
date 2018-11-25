price = float(input("What is the price of your product?"))
sales = float(input("What is the sales tax (in percent value)?"))
sales = sales/100 + 1
cost = price*sales
if cost >= 1:
    print("Your final cost is", cost, "dollars.")
else:
    print("Your final cost is", cost, "cents.")
