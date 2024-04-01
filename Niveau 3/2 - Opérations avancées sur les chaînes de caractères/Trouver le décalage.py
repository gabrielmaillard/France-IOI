def maximum_array(array):
    max_index = 0
    for i in range(len(array)):
        if array[i] > array[max_index]:
            max_index = i
    
    return max_index

def most_common_letter(text):
    array = [0] * 26
    for letter in text:
        if (letter.isalpha()):
            array[ord(letter.upper()) - 65] += 1
    
    return chr(maximum_array(array) + 65)

def getShift(common_letter, supposed_letter):
    return abs(
        ord(common_letter.upper()) - ord(supposed_letter.upper())
    )

def decode_page(page, shift):
    decoded_page = ''
    for char in page:
        if char.isalpha():
            upper = char.isupper()
            char = char.lower()
            decoded_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            if upper:
                decoded_char = decoded_char.upper()
        else:
            decoded_char = char
        decoded_page += decoded_char
    return decoded_page
ligne = input()
print(decode_page(ligne, getShift(most_common_letter(ligne), "e")))