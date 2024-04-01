import sys

def node_height(tree, node):
    height = 0
    while node != 0:
        node = tree[node - 1]
        height += 1
    return height

def recursive_traversal(pattern, combinations, position):
    if position >= len(pattern):
        return
    
    for r in range(len(combinations)):
        if pattern[position] == "?":
            for i in range(1, 10):
                combinations.append(combinations[r] + str(i))
            if position != 0:
                combinations[r] += "0"
            else:
                combinations.pop(r)
        else:
            combinations[r] += pattern[position]
    
    recursive_traversal(pattern, combinations, position + 1)
    return combinations

def main():
    N = int(sys.stdin.readline())
    pattern = list(map(int, sys.stdin.readline().split()))
    search_pattern = sys.stdin.readline()
    combinations = [""]
    combinations = recursive_traversal(search_pattern, combinations, 0)
    possibilities_tpp = [[] for _ in range(N + 1)]
    
    for i in combinations:
        if int(i) <= len(pattern):
            possibilities_tpp[node_height(pattern, int(i))].append(int(i))
    
    for possibilities in possibilities_tpp:
        for possibility in possibilities:
            sys.stdout.write(str(possibility) + " ")

main()
