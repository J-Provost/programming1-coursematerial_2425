def spellcheck(document, valid_words):
    """
    Finds words in the document that are not in the valid words list.

    Parameters:
        document (str): A string containing lines of space-separated words.
        valid_words (list): A list of lowercase valid English words.

    Returns:
        set: A set of words from the document that are not in valid_words.
    """
    # Convert the valid_words list into a set for fast lookups
    valid_set = set(valid_words)
    
    # Split the document into words and convert to lowercase
    words_in_document = document.lower().split()
    
    # Return the set of words not in valid_set
    return {word for word in words_in_document if word not in valid_set}
