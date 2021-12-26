"""
import sys
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
min = nums[0]
max = nums[0]
for num in nums[1:]:
    max = num if num > max else max
    min = num if num < min else min
sys.stdout.write(str(min) + " " + str(max))
"""

"""
import sys
max = 0
for i in range(9):
    num = int(sys.stdin.readline())
    if num > max:
        max = num
        maxi = i+1
print(max)
print(maxi)




from sys import stdin as si
count = [0]*10
a = int(si.readline())
b = int(si.readline())
c = int(si.readline())
mul = a*b*c
while mul > 0:
    count[mul%10]+=1
    mul//=10
for i in range(10):
    print(count[i])



from sys import stdin as si
count = [0]*42
for i in range(10):
    num = int(si.readline())
    count[num%42]+=1
cnt = 0
for i in range(42):
    cnt += 1 if count[i]>0 else 0

print(cnt)




from sys import stdin as si
n = int(si.readline())
avg = 0
max = 0
scores = list(map(int,si.readline().split()))
for i in range(n):
    avg += scores[i]
    max = scores[i] if scores[i] > max else max
avg = (avg/max)*100/n
print(avg)



from sys import stdin as si
n = int(si.readline())
for i in range(n):
    grading = si.readline().rstrip()
    score = 0
    point = 1
    for S in grading:
        if S=='X':
            point = 1
        else:
            score += point
            point+=1
    print(score)




"""
from sys import stdin as si
n = int(si.readline())
for i in range(n):
    scores = list(map(int,si.readline().split()))
    avg = 0
    for j in scores[1:]:
        avg += j
    avg /= scores[0]
    cnt = 0
    for j in scores[1:]:
        cnt = cnt + (1 if j > avg else 0)
    print("{:.3f}%".format(cnt/scores[0]*100))
