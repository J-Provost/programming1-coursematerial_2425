def to_roman(n):
    roman_numerals = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    
    result = []
    
    for value, symbol in roman_numerals:
        while n >= value:
            result.append(symbol)
            n -= value
    
    return ''.join(result)

def from_roman(string):
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(string): 
        value = roman_map[char]
        
        if value < prev_value:
            total -= value
        else:
            total += value
        
        prev_value = value
    
    return total
