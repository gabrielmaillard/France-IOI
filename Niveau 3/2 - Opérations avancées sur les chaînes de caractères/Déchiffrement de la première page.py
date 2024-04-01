decoding_grid = input()
encrypted_text = input()
decoded_text = [0] * len(encrypted_text)
for i in range(len(encrypted_text)):
    if (encrypted_text[i].isalpha()):
        if (encrypted_text[i].isupper()):
            decoded_text[i] = decoding_grid[ord(encrypted_text[i].upper()) - 65].upper()
        else:
            decoded_text[i] = decoding_grid[ord(encrypted_text[i].upper()) - 65].lower()
    else:
        decoded_text[i] = encrypted_text[i]
print("".join(decoded_text))