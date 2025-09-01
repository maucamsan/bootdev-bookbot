from stats import number_of_words
from stats import character_ocurrence
from stats import sorted_dictionaries

def get_book_text(filepath):
    contents = ""
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    relative_path_to_book = 'books/frankenstein.txt'
    word_count = number_of_words(get_book_text(relative_path_to_book))
    char_count = character_ocurrence(get_book_text(relative_path_to_book))
    sorted_dict_list = sorted_dictionaries(character_ocurrence(get_book_text(relative_path_to_book)))

    header = "============ BOOKBOT ============"
    analyzing_message = f"Analyzing book found at {relative_path_to_book}..."
    word_count_header = "----------- Word Count ----------"
    num_word_report = f"Found {word_count} total words"
    character_count_header = "--------- Character Count -------"
    end_header = "============= END ==============="
    print(header, analyzing_message, word_count, num_word_report, character_count_header, sep="\n")

    for c in sorted_dict_list:
        print(f"{c['char']}: {c['num']}")

    print(end_header)

main()
