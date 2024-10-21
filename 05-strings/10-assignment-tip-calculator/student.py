# write your code here
def tip_calculator():
    total = int(input("Enter total price: "))
    tip = input("Enter tip percentage (default=20): ")
    if tip=='':
        tip=20
    else:
        tip = int(tip)
    
    totaal = round(total + (total*(tip/100)))
    return print(f"You have to pay {totaal}")
