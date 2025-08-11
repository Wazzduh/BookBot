from stats import counts_words
from stats import counts_char
from stats import sorting

def get_book_text (path_to_file):
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
        return(file_contents)

def main ():   
    library_of_letters = {} 
    path_to_file = "books/frankenstein.txt"
    contents = get_book_text(path_to_file)
    word_count = counts_words(contents)
    library_of_letters = counts_char(contents)
    sorted_library = sorting(library_of_letters)
    print(f"Found {word_count} total words")
    for key, value in sorted_library.items():
        print(f"{key}: {value}")
main()