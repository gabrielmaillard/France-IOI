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

num_pages = int(input())

for page_num in range(2, num_pages + 1):
    page_text = input()
    if page_num % 2 == 0:
        shift = 3 * page_num
    else:
        shift = -5 * page_num
    decoded_page = decode_page(page_text, shift)
    print(decoded_page)