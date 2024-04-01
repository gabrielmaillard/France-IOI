N = int(input())
power_maximum_value = 1
num_figures = 0
while power_maximum_value <= N:
    power_maximum_value = power_maximum_value * 2
    num_figures += 1
max_ = (power_maximum_value//2)
if N == 0:
    print(0)
while N != 0 or num_figures > 0:
    if max_ <= N:
        print(1, end="")
        N -= max_
        max_ //= 2
    else:
        print(0, end="")
        max_ //=2
    num_figures -= 1