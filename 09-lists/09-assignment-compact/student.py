def compact(xs):
    return [x for x in xs if x is not None]
def compact_in_place(xs):
    i = 0
    while i < len(xs):
        if xs[i] is None:
            xs.pop(i) 
        else:
            i += 1 
