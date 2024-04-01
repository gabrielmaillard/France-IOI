def generate_array(size):
    tbl = []
    for i in range(size):
        tbl.append(tuple(i for i in map(int, input().split(" "))))
    return tbl
print(*("{} {}".format(i[0], i[1]) for i in [list(element) for element in (sorted(generate_array(int(input())), key=lambda sl: (sl[1],sl[0])))]), sep="\n")