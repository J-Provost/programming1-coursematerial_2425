def remove_runs(ns):
    if not ns: 
        return []
    
    result = [ns[0]]
    last_element = ns[0]
    
    for elem in ns[1:]:
        if elem != last_element:
            result.append(elem)
            last_element = elem 
    
    return result
