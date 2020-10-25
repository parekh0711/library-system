from math import *
t = int(input())
for _ in range(t):
    n = int(input())
    sol1 = (-1+sqrt(1+24*n))/6
    sol2 = (-1-sqrt(1+24*n))/6
    sol = max(sol1,sol2)
    print(floor(sol))
