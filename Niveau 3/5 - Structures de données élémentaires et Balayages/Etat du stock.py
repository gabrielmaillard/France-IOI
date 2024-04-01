num_products = int(input())
available_products = list(map(int, input().split(" ")))
num_operations = int(input())
for i in range(num_operations):
   np, qty = map(int, input().split(" "))
   available_products[np-1] += qty
print(" ".join(map(str, available_products)))