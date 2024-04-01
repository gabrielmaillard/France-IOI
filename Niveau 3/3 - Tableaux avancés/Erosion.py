def generate_image(H, L):
    image = [['.' for _ in range(L)] for _ in range(H)]
    for line in range(H):
        image[line] = list(input())
    return image

def print_image(image):
    for line in image:
        for column in line:
            print(column, end="")
        print()

def erode_image(image):
    new_image = [['.' for _ in range(len(image[0]))] for _ in range(len(image))]
    for iLine in range(len(image)):
        for iColumn in range(len(image[0])):
            current_pixel = image[iLine][iColumn]
            if (current_pixel == "#"):
                deltas = [
                    (-1, 0),
                    (0, -1),
                    (0, 1),
                    (1, 0),
                ]
                nNeighboursFull = 0
                for delta in deltas:
                    newLine = iLine + delta[0]
                    newColumn = iColumn + delta[1]
                    if (
                        0 <= newLine < len(image)
                        and
                        0 <= newColumn < len(image[0])
                    ):
                        comparison = image[newLine][newColumn]
                        if (comparison == "#"):
                            nNeighboursFull += 1
                if (nNeighboursFull == 4):
                    new_image[iLine][iColumn] = "#"
                else:
                    new_image[iLine][iColumn] = "."
    return new_image
N = int(input())
H, L = map(int, input().split(" "))
produced_image = generate_image(H, L)
for i in range(N):
    produced_image = erode_image(produced_image)
print_image(produced_image)