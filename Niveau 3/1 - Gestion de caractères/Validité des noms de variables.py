num_names = int(input())

def acceptable(pL):
    pL = pL.upper()
    codeASCII = ord(pL) - 64
    if not ((codeASCII <= 26 and codeASCII >= 1) or pL == "_"):
        return False
    return True

def check_word(word):
    if not acceptable(word[0]):
        return "NO"
    
    for letter in word:
        if not (
            acceptable(letter)
            or letter.isdigit()
        ):
            return "NO"
    
    return "YES"
    
for i in range(num_names):
    print(check_word(input()))