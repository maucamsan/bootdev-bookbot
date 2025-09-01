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

def sort_on(items):
    return items["num"]

def sorted_dictionaries(dict_to_sort):
    report_list = []
    for pair in dict_to_sort:
        if pair.isalpha():
            report_list.append({"char": pair, "num": dict_to_sort[pair]})
    report_list.sort(reverse=True, key=sort_on)
    return report_list