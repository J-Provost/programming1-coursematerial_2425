# write your code here
from math import floor
def cake2(eggs, flour):
    flour = flour//250
    eggs = eggs//5
    if eggs<flour:
        return eggs
    else: 
        return flour
