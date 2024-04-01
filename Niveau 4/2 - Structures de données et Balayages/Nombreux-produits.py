import sys

def main():
    num_distributors = int(sys.stdin.readline())
    num_operations = int(sys.stdin.readline())
    distributors = [[] for _ in range(num_distributors)]
    
    for _ in range(num_operations):
        distributor_id, quantity, deadline = map(int, sys.stdin.readline().split())
        distributor_id -= 1
        
        if deadline != 0:
            distributors[distributor_id].append((quantity, deadline))
        else:
            while quantity < 0:
                qty, date = distributors[distributor_id].pop(0)
                quantity += qty
            if quantity > 0:
                distributors[distributor_id].insert(0, (quantity, date))
    
    for i in range(num_distributors):
        if not distributors[i]:
            sys.stdout.write("0\n")
            continue
        min_deadline = min(date for _, date in distributors[i])
        sys.stdout.write(str(min_deadline) + "\n")

main()