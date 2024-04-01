import sys

N = int(sys.stdin.readline().strip())
code_to_code = [0] + list(map(int, sys.stdin.readline().split()))

def find_common_recipient(code1, code2):
    visited = set()
    
    while code1 != 0 or code2 != 0:
        if code1 != 0:
            if code1 in visited:
                return code1
            visited.add(code1)
            code1 = code_to_code[code1]
        if code2 != 0:
            if code2 in visited:
                return code2
            visited.add(code2)
            code2 = code_to_code[code2]
    
    return 0

R = int(sys.stdin.readline().strip())

for _ in range(R):
    code1, code2 = map(int, sys.stdin.readline().split())
    result = find_common_recipient(code1, code2)
    sys.stdout.write(str(result) + "\n")
