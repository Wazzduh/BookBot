import sys
from stats import counts_words
from stats import counts_char
from stats import sorting

def get_book_text (path_to_file):
    with open(path_to_file) as f:
        # f is a file object
        file_contents = f.read()
        return(file_contents)

def main ():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    library_of_letters = {}
    contents = get_book_text(sys.argv[1])
    word_count = counts_words(contents)
    library_of_letters = counts_char(contents)
    sorted_library = sorting(library_of_letters)
    print(f"Found {word_count} total words")
    for key, value in sorted_library.items():
        print(f"{key}: {value}")
main()