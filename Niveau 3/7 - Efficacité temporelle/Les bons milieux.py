import sys

def main():
    mid_points_count = 0
    num_points = int(sys.stdin.readline())
    points_set = set()
    points_list = []
    
    for i in range(num_points):
        x, y = map(int, sys.stdin.readline().split())
        points_set.add((x, y))
        points_list.append([x, y])
    
    used_points = set()
    for i in range(num_points):
        x1, y1 = points_list[i]
        for j in range(i + 1, num_points):
            x2, y2 = points_list[j]
            sum_x = x1 + x2
            sum_y = y1 + y2
            mid_x = sum_x / 2
            mid_y = sum_y / 2
            if sum_x % 2 == 0 and sum_y % 2 == 0 and (mid_x, mid_y) in points_set and (mid_x, mid_y) not in used_points:
                mid_points_count += 1
                used_points.add((mid_x, mid_y))
    sys.stdout.write(str(mid_points_count))

main()
