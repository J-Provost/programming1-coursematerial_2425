# write your code here
def is_capitalized(string):
    result=False
    if not string:
        result=False
    elif string[0] == string[0].upper():
        if string[1:]==string[1:].lower():
            result = True
    return result
    