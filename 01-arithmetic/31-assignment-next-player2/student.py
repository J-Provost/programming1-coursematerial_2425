# write your code here
#def next_player2(player, player_count):
#    next = player + 1
#    if next > player_count:
#        return 1
#    else:
#        return next
def next_player2(player, player_count):
    next= player+1
    result = next%(player_count+1)
    return result