import sys

def build_tree(products):
    tree = {0: []}
    for product, container in enumerate(products, 1):
        if container not in tree:
            tree[container] = []
        tree[container].append(product)
    return tree

def tree_height(tree, node):
    stack = [(node, 1)]
    max_height = 0
    while stack:
        node, height = stack.pop()
        if node in tree:
            for child in tree[node]:
                stack.append((child, height + 1))
        max_height = max(max_height, height)
    return max_height

def main():
    sys.stdin.readline()
    products = list(map(int, sys.stdin.readline().split()))
    tree = build_tree(products)
    print(tree_height(tree, 0) - 1)

main()
