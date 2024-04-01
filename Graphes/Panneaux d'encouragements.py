num_lines, num_columns = map(int,input().split())

labyrinth = [list(input()) for _ in range(num_lines)]
labyrinth[1][0] = 'E'
labyrinth[num_lines-1][num_columns-2] = 'S'
distance = int(input())

next_cell = []

def mark(x,y):
    if labyrinth[x][y] != '.':
        return False
    labyrinth[x][y] = 'o'
    next_cell.append( (x,y) )
    return True

mark(num_lines-2,num_columns-2)
print(len(next_cell),end=" ")

for _ in range(1,distance):
    num_signs = 0
    cells = next_cell
    next_cell = []
    for lig,col in cells:
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            x = lig + dx
            y = col + dy
            if mark(x,y) or labyrinth[x][y] == 'E':
                num_signs += 1
    print(num_signs,end=" ")