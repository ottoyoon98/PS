from collections import deque

apples = []
keys = []
way = ((0, 1), (1, 0), (0, -1), (-1, 0))
dir = {'L':-1, 'D':1}
snake_dir = 0
snake = deque()
snake.append((1, 1))
time = 0
index = 0

n = int(input())
for _ in range(int(input())):
    apples.append(tuple(map(int, input().split())))
    
for _ in range(int(input())):
    temp = input().split()
    keys.append(tuple((int(temp[0]), temp[1])))

while True:
    if index < len(keys) and keys[index][0] == time:
        snake_dir = (snake_dir+4+dir[keys[index][1]])%4
        index+=1
    time+=1
    next = (snake[-1][0]+way[snake_dir][0],
            snake[-1][1]+way[snake_dir][1])
    if next in snake or next[0] < 1 or next[0] > n or next[1] < 1 or next[1] > n:
        break
    snake.append(next)
    if next in apples:
        apples.remove(next)
    else:
        snake.popleft()
        
print(time)