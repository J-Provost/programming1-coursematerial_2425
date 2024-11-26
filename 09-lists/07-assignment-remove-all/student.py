def remove_all(xs, item_to_remove):
    i = len(xs) - 1
    while i >= 0:
        if xs[i] == item_to_remove:
            xs.pop(i)
        i -= 1
