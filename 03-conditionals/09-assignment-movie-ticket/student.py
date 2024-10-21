# write your code here
from math import ceil
def movie_ticket(duration, imax, student, ticket_count):
    if duration<=90:
        cost=10
    elif duration<=120:
        cost=11
    elif duration<=150:
        cost=12
    else:
        cost=15
    if imax:
        cost = ceil(cost*1.2)
    if student:
        cost-=3
    return cost*ticket_count 