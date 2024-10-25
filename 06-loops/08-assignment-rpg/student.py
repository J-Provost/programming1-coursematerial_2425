def rpg2(n_sides, goal):
    count = 0
    for i in range(1,n_sides+1):
        for y in range(1,n_sides+1):
            if (i+y)>=goal:
                count+=1
    total_pos=n_sides*n_sides
    kans=count/total_pos*100
    return kans
    
def rpg3(n_sides, goal):
    count = 0
    for i in range(1,n_sides+1):
        for y in range(1,n_sides+1):
            for x in range(1,n_sides+1):
                if (i+y+x)>=goal:
                    count+=1
    total_pos=n_sides*n_sides*n_sides
    kans=count/total_pos*100
    return kans    
