# write your code here
def split_in_two(xs):
    split_point = (len(xs) + 1) // 2
    left_half = xs[:split_point]
    right_half = xs[split_point:]
    return (left_half, right_half)