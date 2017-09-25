from helpers import alphabet_position, rotate_character

def rotate_string(text, rot):
    encrypted_str = ''
    for l in text:
        rotated = rotate_character(l,rot)
        encrypted_str = encrypted_str + rotated

    return encrypted_str

def main():
    text = input('Type a message: ')
    rot = input('Rotate by: ')
    rot_int = int(rot)
    encrypted = rotate_string(text, rot_int)
    print(encrypted)

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

if __name__ == "__main__":
    main()