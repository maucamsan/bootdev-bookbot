def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    return contents

def number_of_words(book):
    list = book.split()
    num_of_words = 0
    return len(list) - 1

def main():
    print(f"{number_of_words(get_book_text('books/frankenstein.txt'))} words found in the document")


main()
