def invest(amount, rate, goal):
    years = 0
    while amount < goal:
        years += 1
        amount += amount * rate/100
    return years
