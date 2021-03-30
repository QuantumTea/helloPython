def concat(string1, string2):
    return string1 + string2


def get_letter_in_string(input_string, index):
    return input_string[index]


def bottles_of_beer(number_of_bottles):
    if type(number_of_bottles) == int:
        if number_of_bottles == 0:
            return "No bottles of beer on the wall, how sad"
        if number_of_bottles == 1:
            return "One bottle of beer on the wall"
        if number_of_bottles >= 2:
            return str(number_of_bottles) + " bottles of beer on the wall"
    else:
        return "This is weird"


def bottles_song(number_of_bottles):
    return number_of_bottles
