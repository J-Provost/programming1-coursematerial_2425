# write your code here
def domino_chain(dominos):
    if not dominos:
        return True
    for i in range(len(dominos) - 1):
        if dominos[i][1] != dominos[i + 1][0]:
            return False
    return True
