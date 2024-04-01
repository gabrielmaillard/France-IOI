from sys import stdin
from math import sqrt

def main():
    x_A,y_A,x_B,y_B = map( int, input().split() )
    x_AB = x_B - x_A
    y_AB = y_B - y_A

    num_points = int(input())

    normAB = sqrt( (x_AB)**2 + (y_AB)**2 )

    max_found = 0
    mX, mY = 0, 0

    for _, description in zip(range(num_points), stdin):
        x_P,y_P = map(int, description.split())

        x_AP = x_P - x_A
        y_AP = y_P - y_A

        distAH = (x_AB * x_AP + y_AB * y_AP) / normAB

        distance = (sqrt(max(distAH**2, (x_AP**2+y_AP**2)) - min(distAH**2, (x_AP**2+y_AP**2))))
        if distance > max_found:
            max_found = distance
            mX = x_P
            mY = y_P
    
    print(mX, mY)

main()