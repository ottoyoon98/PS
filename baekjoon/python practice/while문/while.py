"""
from sys import stdin as si, stdout as so
begin = int(si.readline())
num = begin
cycle = 0
while True:
    num = (num%10)*10+(num//10+num%10)%10
    cycle+=1
    if num == begin:
        break
so.write(str(cycle))
"""

from sys import stdin as si, stdout as so
while True:
    try:
        a, b = list(map(int,si.readline().split()))
        so.write(str(a+b)+"\n")
    except:
        break
