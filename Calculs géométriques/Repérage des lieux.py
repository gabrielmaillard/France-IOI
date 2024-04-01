from sys import stdin
from math import sqrt

def main():
    x_A,y_A,x_B,y_B = map(int, input().split())
    x_AB = x_B - x_A
    y_AB = y_B - y_A
    nbPoints = int(input())
    normAB = sqrt((x_AB)**2 + (y_AB)**2)
    for _,description in zip(range(nbPoints),stdin):
        x_P,y_P = map(int, description.split())
        x_AP = x_P - x_A
        y_AP = y_P - y_A
        print((x_AB * x_AP + y_AB * y_AP) / normAB)

main()