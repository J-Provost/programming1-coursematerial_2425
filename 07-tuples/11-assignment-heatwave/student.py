# write your code here
def heatwave(temperatures):
    n = len(temperatures)
    count_25_plus = 0 
    count_30_plus = 0 
    for temp in temperatures:
        if temp >= 25:
            count_25_plus += 1
            if temp >= 30:
                count_30_plus += 1
            if count_25_plus >= 5 and count_30_plus >= 3:
                return True
        else:
            count_25_plus = 0
            count_30_plus = 0

    return False
