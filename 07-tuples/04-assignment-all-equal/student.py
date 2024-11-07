# write your code here
def all_equal(xs):
    result = True
    for index in range(len(xs)):
        result = xs[0]== xs[index] and result
    return result