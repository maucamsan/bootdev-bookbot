def number_of_words(book):
    list = book.split()
    num_of_words = 0
    return len(list) - 1

def character_ocurrence(text_from_book):
    ocurrences = {}
    for c in text_from_book:
        c_lowered = c.lower()
        if c.lower() in ocurrences:
            ocurrences[c_lowered] += 1
        else:
            ocurrences[c_lowered] = 1
    return ocurrences

