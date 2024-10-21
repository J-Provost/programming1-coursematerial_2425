# write your code here
from math import ceil
def internet_costs(duration_in_seconds, cost_per_block):
    x = ceil(duration_in_seconds/360)
    result = cost_per_block * x
    return result