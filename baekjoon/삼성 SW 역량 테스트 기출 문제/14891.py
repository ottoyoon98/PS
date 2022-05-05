#14891 톱니바퀴
from collections import deque
gear = [deque(input()) for i in range(4)]
K = int(input())
#dir  0:left 1:right 2:both(starting point)
def rotate(index, rd, dir):
    if dir==2 or dir==1:
        if index < 3 and gear[index][2] != gear[index+1][6]:
            rotate(index+1, -rd, 1)
    if dir==2 or dir==0:
        if index > 0 and gear[index-1][2] != gear[index][6]:
            rotate(index-1, -rd, 0)
    gear[index].rotate(rd)
    
for i in range(K):
    N, T = map(int, input().split())
    rotate(N-1, T, 2)
sum=0
mul=1
for i in range(4):
    sum+=int(gear[i][0])*mul
    mul*=2
print(sum)