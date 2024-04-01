def draw_sierpinski_triangle(size, x, y, image):
    if size == 1:
        image[y][x] = '#'
    else:
        draw_sierpinski_triangle(size // 2, x, y, image)
        draw_sierpinski_triangle(size // 2, x + size // 2, y, image)
        draw_sierpinski_triangle(size // 2, x, y + size // 2, image)
def main():
    N = int(input())
    image = [[' ' for _ in range(N)] for _ in range(N)]
    draw_sierpinski_triangle(N, 0, 0, image)
    for row in image:
        print(''.join(row).rstrip())
main()