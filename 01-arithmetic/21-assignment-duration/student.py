# write your code here
def hours(duration):
    h = duration//3600
    return h

def minutes(duration):
    h = hours(duration)
    x = duration - (h*3600)
    m = x//60
    return m

def seconds(duration):
    h = hours(duration)
    m = minutes(duration)
    s = duration - (m*60) -(h*3600)
    return s