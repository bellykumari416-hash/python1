actual_cost = float(input(" please enter the actual product price: "))
sale_amount = float(input(" please enter the sale product price: "))

if (sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Total pofiit = {0}".format(amount))
else:
    print("No profit!!!!")

