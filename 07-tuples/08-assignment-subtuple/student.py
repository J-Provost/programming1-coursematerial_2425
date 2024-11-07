# write your code here
def subtuple(xs, ys):
    if len(ys) == 0:
        return True
    if len(ys) > len(xs):
        return False
    for index in range(len(xs) - len(ys) + 1):
        if xs[index:index + len(ys)] == ys:
            return True
    return False
