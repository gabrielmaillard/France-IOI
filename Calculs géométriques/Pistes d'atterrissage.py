from sys import stdin
import math

def main():
    x_P, y_P = map(int, input().split())
    num_points = int(input())

    max_X = float("inf")

    Xi1, Yi1, Xi2, Yi2 = 0, 0, 0, 0

    for _,description in zip(range(num_points),stdin):
        x_A,y_A,x_B,y_B = map( int, description.split() )

        x_AB = x_B - x_A
        y_AB = y_B - y_A
        normAB = math.sqrt( (x_AB)**2 + (y_AB)**2 )
        
        x_AP = x_P - x_A
        y_AP = y_P - y_A
        distAH = (x_AB * x_AP + y_AB * y_AP) / normAB
        
        if distAH < 0:
            distAH = 0
        elif distAH > normAB:
            distAH = normAB
        
        a = distAH**2
        b = x_AP**2 + y_AP**2

        distance = math.sqrt(max(a, b) - min(a, b))
        if distance < max_X:
            max_X = distance
            Xi1 = x_A
            Yi1 = y_A
            Xi2 = x_B
            Yi2 = y_B
    print(Xi1, Yi1, Xi2, Yi2)

main()