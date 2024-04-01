def paintRectangle(image, L1, L2, C1, C2, color):
    for lineC in range(len(image)):
        for columnC in range(len(image[lineC])):
            
            if (
                (lineC >= L1) and
                (lineC <= L2) and
                (columnC >= C1) and
                (columnC <= C2)
            ):
                image[lineC][columnC] = color

num_lines, num_columns = map(int, input().split(" "))
image = [['.' for _ in range(num_columns)] for _ in range(num_lines)]
num_rectangles = int(input())

for i in range(num_rectangles):
    infos = input().split(" ")
    L1, C1, L2, C2 = map(int, infos[0:4])
    color = infos[4]
    paintRectangle(image, L1, L2, C1, C2, color)

for line in image:
    for column in line:
        print(column, end="")
    print()