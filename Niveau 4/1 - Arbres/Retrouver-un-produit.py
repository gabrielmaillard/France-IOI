num_objects = int(input())
code_to_code = ["."] + list(map(int, input().split()))

def code_to_code_recursive(code_): 
    if code_to_code[code_] == 0:
        print(code_, end=" ")
    else:
        code_to_code_recursive(code_to_code[code_])
        print(code_, end=" ")

int(input())
searched_codes = list(map(int, input().split()))

for code_searched in searched_codes:
    code_to_code_recursive(code_searched)
    print()
