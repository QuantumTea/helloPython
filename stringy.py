def concat(string1, string2):
    return string1 + string2


def get_letter_in_string(input_string, index):
    return input_string[index]


def bottles_of_beer(number_of_bottles):
    if type(number_of_bottles) == int:
        if number_of_bottles != 0:
            return "one bottle of beer on the wall"
        elif number_of_bottles == 1:
            return "No bottles of beer on the wall, how sad."
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
