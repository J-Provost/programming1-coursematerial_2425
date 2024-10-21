# write your code here
def player_movement(position, left_arrow, right_arrow, shift):
    if left_arrow==True and right_arrow==False and shift==False:
        position-=1
    elif left_arrow==False and right_arrow==True and shift==False:
        position+=1
    elif left_arrow==True and right_arrow==False and shift==True:
        position-=2
    elif left_arrow==False and right_arrow==True and shift==True:
        position+=2
    return position