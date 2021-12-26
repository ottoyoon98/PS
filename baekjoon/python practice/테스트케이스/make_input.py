from sys import stdin as si, stdout as so
"""
f = open('input.txt', 'w')
f.write("500000\n")
for i in range(500000):
    f.write(str(i*20)+" ")
f.write("\n500000\n")
for i in range(500000):
    f.write(str(i*20))
    f.write(" ")
f.write("\n")

f.close()
"""
import random
random.seed()
n, m = map(int,input().split())
for i in range(n):
    print(random.randrange(1,1000000))
