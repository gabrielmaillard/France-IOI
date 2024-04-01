def area_intersection(A, B, C, D):
    x_inter_min = max(A[0], C[0])
    y_inter_min = max(A[1], C[1])
    x_inter_max = min(B[0], D[0])
    y_inter_max = min(B[1], D[1])

    width_inter = max(0, x_inter_max - x_inter_min)
    height_inter = max(0, y_inter_max - y_inter_min)

    area_inter = width_inter * height_inter
    return area_inter

A0, A1, B0, B1 = map(int, input().split())
total_area = (A1 - B1) * (A0 - B0)

point_A = (A0, A1)
point_B = (B0, B1)

N = int(input())
for _ in range(N):
    C0, C1, D0, D1 = map(int, input().split())
    total_area -= area_intersection(point_A, point_B, (C0, C1), (D0, D1))

print(total_area)