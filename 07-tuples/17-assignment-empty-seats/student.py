def empty_seats(used_seats):
    if len(used_seats) < 2:
        return 0
    empty_count = 0
    for i in range(1, len(used_seats)):
        empty_count += used_seats[i] - used_seats[i - 1] - 1

    return empty_count
