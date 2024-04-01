def solve_hanoi(nbPlates, start, intermediate, end):
    if nbPlates == 1:
        print(start, "->", end)
    else:
        solve_hanoi(nbPlates - 1, start, end, intermediate)
        print(start, "->", end)
        solve_hanoi(nbPlates-1, intermediate, start, end)
solve_hanoi(int(input()), 1, 2, 3)