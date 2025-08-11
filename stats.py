from operator import itemgetter

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

def sorting(library):
    alpha = {key: value for key, value in library.items() if key.isalpha()}
    sorted_item = sorted(alpha.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = dict(sorted_item)
    return sorted_dict