X1D1, Y1D1, X2D1, Y2D1 = map(int, input().split())
X1D2, Y1D2, X2D2, Y2D2 = map(int, input().split())
Xres = 0
Yres = 0
if X1D1 == X2D1:
    Xres = X1D1
    m = (Y1D2 - Y2D2) / (X1D2 - X2D2)
    b = Y1D2 - m * X1D2
    Yres = m * Xres + b
elif X2D2 == X1D2:
    Xres = X2D2
    m = (Y1D1 - Y2D1) / (X1D1 - X2D1)
    b = Y1D1 - m * X1D1
    Yres = m * Xres + b
else:
    m1 = (Y1D1 - Y2D1) / (X1D1 - X2D1)
    b1 = Y1D1 - m1 * X1D1
    m2 = (Y1D2 - Y2D2) / (X1D2 - X2D2)
    b2 = Y1D2 - m2 * X1D2
    Xres = (b2 - b1) / (m1 - m2)
    Yres = m2 * Xres + b2
print(Xres, Yres)