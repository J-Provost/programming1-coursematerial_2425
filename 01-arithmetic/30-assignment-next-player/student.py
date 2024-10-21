# write your code here
#def next_player(player, player_count):
#    next = player + 1
#    if next == player_count:
#        return 0
#    else:
#        return next
def next_player(player, player_count):
    next= player+1
    result = next%player_count
    return result