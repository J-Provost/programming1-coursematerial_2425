# write your code here
def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    x = eggs // eggs_per_cake
    y = flour // flour_per_cake
    z = butter // butter_per_cake
    q = sugar // sugar_per_cake
    return min(x,y,z,q)