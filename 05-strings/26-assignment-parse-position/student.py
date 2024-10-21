# write your code here
def parse_position_x(string):
    string= string.strip('()')
    position=string.find(",")
    x=float(string[0:position])
    return x

def parse_position_y(string):
    string= string.strip('()')
    position = string.find(",")+2
    y = float(string[position:])
    return y
