def remove_backspaces(string):
    result = ""
    for i in range(len(string)):
        if string[i] == '\b':
            result = result[:-1]
        else:
            result += string[i]
    
    return result
