# write your code here
def total_cost(amount):
    cost= amount 
    if amount<100:
        cost+=10
    if amount>=200:
        cost=amount*0.95
    return cost
    
