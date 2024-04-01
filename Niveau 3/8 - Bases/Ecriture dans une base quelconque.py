N, base = map(int, input().split())
power_maximum_value = 1
i = 0
while power_maximum_value <= N:
    power_maximum_value = power_maximum_value * base
    i += 1
if i == 0:
   print(1)
   print(0)
else:
   print(i)
   iMax = i
   while i >= 0:
       n = N//(base**i)
       if n > 0 or i < iMax:
           print(n, end=" ")
       N = N%(base**i)
       i -= 1