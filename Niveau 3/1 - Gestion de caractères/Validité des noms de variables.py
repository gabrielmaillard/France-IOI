num_names = int(input())

def acceptable(pL):
    pL = pL.upper()
    codeASCII = ord(pL) - 64
    if not ((codeASCII <= 26 and codeASCII >= 1) or pL == "_"):
        return False
    return True

def check_word(mot):
    if not acceptable(mot[0]):
        return "NO"
    
    for lettre in mot:
        if not (
            acceptable(lettre)
            or lettre.isdigit()
        ):
            return "NO"
    
    return "YES"
    
for i in range(num_names):
    print(check_word(input()))