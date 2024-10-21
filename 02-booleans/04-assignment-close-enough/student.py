# write your code here
def close_enough(x, y):
    laagste = min(x,y)
    hoogste = max(x,y)
    verschil = hoogste - laagste
    if verschil<=0.1:
        return True
    else:
        return False
