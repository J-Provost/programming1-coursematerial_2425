def contains_duplicates(xs):
    seen = set() 
    for item in xs:
        if item in seen:
            return True
        seen.add(item)
    return False