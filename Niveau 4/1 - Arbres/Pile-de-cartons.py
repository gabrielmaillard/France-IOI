import sys

num_boxes = int(sys.stdin.readline())
tree = []

for _ in range(num_boxes + 1):
    tree.append(list(map(int, sys.stdin.readline().split()))[1:])

def traverse_entire_tree(global_tree, subtree):
    for node in subtree:
        sys.stdout.write("A " + str(node) + "\n")
        traverse_entire_tree(global_tree, global_tree[node])
        sys.stdout.write("R " + str(node) + "\n")

traverse_entire_tree(tree, tree[0])
