def concat(string1, string2):
    # trim strings, add one space back
    return string1.strip() + " " + string2.strip()


def get_letter_in_string(input_string, index):
    try:
        return input_string[index]
    except IndexError:
        # catch one specific error type
        return "Error, index out of bounds"


def bottles_of_beer(number_of_bottles):
    if type(number_of_bottles) == int:
        if number_of_bottles == 0:
            return "No bottles of beer on the wall, how sad"
        elif number_of_bottles == 1:
            return "One bottle of beer on the wall"
        elif number_of_bottles < 0:
            return "Go to the store and buy some more"
        elif number_of_bottles >= 2:
            return str(number_of_bottles) + " bottles of beer on the wall"
    else:
        return "This is weird"


def bottles_song(number_of_bottles):
    whole_song = ""

    for i in range(number_of_bottles, -1, -1):
        whole_song = whole_song + bottles_of_beer(i) + "\n"

    print(whole_song)
    return whole_song


def is_string_in_text(text_to_search, search_term):
    if text_to_search.find(search_term) != -1:
        return True
    else:
        return False


def where_in_string_is_text(text_to_search, search_term):
    if text_to_search.find(search_term) == -1:
        return "Search string not found"

    # split on spaces
    tokenised_string = text_to_search.split()
    return tokenised_string.index(search_term)
