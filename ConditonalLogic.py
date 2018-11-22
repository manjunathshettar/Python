def ground_shipping_cost(weight):
  if weight <= 2:
    cost = weight*1.50 + 20
    return cost
  elif weight > 2 and weight <= 6:
    cost = weight*3.00 + 20
    return cost
  elif weight > 6 and weight <= 10:
    cost = weight*4.00 + 20
    return cost
  else:
    cost = weight*4.75 + 20
    return cost
print(ground_shipping_cost(8.4))
premium = 125.00

def drone_price(weight):
  if weight <= 2:
    cost = weight*4.5
    return cost
  elif weight > 2 and weight <= 6:
    cost = weight*9
    return cost
  elif weight > 6 and weight <= 10:
    cost = weight*12
    return cost
  else:
    cost = 14.25*weight
    return cost

print(drone_price(1.5))

def lowest(weight):
  scost = ground_shipping_cost(weight)
  dcost = drone_price(weight)
  if scost < dcost and scost < premium:
    print("The ground shipping method is the cheapest and costs "+ 	str(scost))
  elif dcost < scost and dcost < premium:
    print("The drone shipping method is the cheapest and costs " + 	str(dcost))
  else:
    print("The premium shipping cost is the cheapest, at $125.")
    
lowest(4.8)
