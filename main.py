from stats import number_of_words
from stats import character_ocurrence

def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    print(f"{number_of_words(get_book_text('books/frankenstein.txt'))} words found in the document")
    print(f"{character_ocurrence(get_book_text('books/frankenstein.txt'))}")


main()
