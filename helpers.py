def alphabet_position(letter):

    a_index = ord(letter) - 97
    A_index = ord(letter) - 65

    if letter.isupper():
        #print("A",A_index)
        return A_index
    else:
        #print("a",a_index)
        return a_index

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    Alphabet = alphabet.upper()
    encrypted = ''
    if char.isupper():
        rotated_index = alphabet_position(char) + rot
        if rotated_index < 26: 
            encrypted = Alphabet[rotated_index]
        else:
            encrypted = Alphabet[rotated_index % 26]
        return encrypted
    elif char.islower():
        rotated_index = alphabet_position(char) + rot
        if rotated_index < 26: 
            encrypted = alphabet[rotated_index]
        else:
            encrypted = alphabet[rotated_index % 26]
        return encrypted
    else:
        return char