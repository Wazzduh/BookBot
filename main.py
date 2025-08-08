from stats import counts_words
from stats import counts_char

def get_book_text (path_to_file):
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
        return(file_contents)

def main ():    
    path_to_file = "books/frankenstein.txt"
    contents = get_book_text(path_to_file)
    word_count = counts_words(contents)
    print(f"{word_count} words found in the document")
    library_of_letters = counts_char(contents)
    print(library_of_letters)

main()