
def counts_words (contents):
    word_count = 0
    split_contents = contents.split()
    for i in split_contents:
        word_count += 1 
    return(word_count)

def counts_char (contents):
    library = {}
    for char in contents:
        char = char.lower()
        if char not in library:
            library[char] = 1  
        else:
            library[char] += 1

    return library