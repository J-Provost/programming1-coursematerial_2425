# write your code here
def increasing(ns):
    result=True
    for index in range(len(ns)-1):
        result= result and ns[index]<=ns[index+1]
    return result