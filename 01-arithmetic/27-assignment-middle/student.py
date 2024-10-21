# write your code here
def middle(a, b, c):
        mini = min(a, b, c)
        maxi = max(a, b, c) 
        total = a+b+c
        middle = total - mini - maxi
        return middle