def est_bien_parenthesee(expression, ouvrants="({[<", fermants=")}]>"):
    stack = []
    for char in expression:
        if char in ouvrants:
            stack.append(char)
        elif char in fermants:
            if not stack or ouvrants.index(stack.pop()) != fermants.index(char):
                return False
    return not stack

expression = input()
print("yes" if est_bien_parenthesee(expression) else "no")