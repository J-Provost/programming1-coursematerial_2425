# write your code here
def coins(amount):
    five = amount//5
    two = (amount - (five*5))//2
    one = (amount - (five*5)-(two*2))
    total = five+two+one
    return total