def gcd(x, y):
    x=abs(x)
    y=abs(y)
    mini=min(x,y)
    greatest=0
    while greatest==0:
        if x%mini==0 and y%mini==0:
            greatest=mini
        mini-=1 
    return greatest

print(gcd(15,9))