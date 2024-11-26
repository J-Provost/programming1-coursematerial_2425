# write your code here
def election_winner(votes):
    if not votes:
        return None
    winner = None
    max_count = 0
    for vote in votes:
        count = 0
        for v in votes:
            if v == vote:
                count += 1
        if count > max_count:
            max_count = count
            winner = vote
    return winner
