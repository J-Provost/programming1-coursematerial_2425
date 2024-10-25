def valid_parentheses(string):
    open=0
    close=0
    for char in string:
        if char == "(":
            open+=1
        elif char==")":
            close+=1
        if close>open:
            return False
    return open==close