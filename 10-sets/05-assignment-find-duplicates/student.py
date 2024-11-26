def find_duplicates(xs):
    """
    Finds all duplicates in the list xs.

    Parameters:
        xs (list): The input list.

    Returns:
        list: A list of duplicates, each mentioned only once.
    """
    seen = set()
    duplicates = set()
    
    for item in xs:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)
