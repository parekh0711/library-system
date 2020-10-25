import random

t = 5000
name = "input3.txt"
print(t,file=open(name,"a+"))
for _ in range(t):
    print(_)
    p = random.randint(0,1000000000)
    q = random.randint(1,1000000000)
    print(p,q,file=open(name, "a+"))
