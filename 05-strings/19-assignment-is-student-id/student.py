# write your code here
def is_student_id(string):
    if string[0]=="r" or string[0]=="R" or string[0]=="s" or string[0]=="S":
        first = True
    else:
        first=False
    digit =is_digit(string[1:])
    return first and digit

def is_digit(char):
    lengte = len(char)
    x=0
    check = True
    if lengte==7 and str.isnumeric(char):
        while x<=6:
            check = check and (0<=int(char[x])<=9)
            x+=1
        return check
    else:
        return False