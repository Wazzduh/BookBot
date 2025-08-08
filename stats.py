
def counts_words (contents):
    word_count = 0
    split_contents = contents.split()
    for i in split_contents:
        word_count += 1 
    return(word_count)