N, M, x, y, K = map(int, input().split())
MAP = [list(map(int, input().split())) for i in range(N)]
dir = ((0, 0), (0, 1), (0, -1), (-1, 0), (1, 0))
dice_x = x
dice_y = y
dice_value = [0,]*6
dice_state = [0, 1, 2]

for mv in map(int, input().split()):
    nx, ny = dice_x+dir[mv][0], dice_y+dir[mv][1]
    if nx < 0 or ny < 0 or nx >= N or ny >= M:
        continue
    #change dice_state
    
    temp = dice_state[0]
    if mv == 1:
        dice_state[0] = dice_state[2]
        dice_state[2] = 5-temp
    elif mv == 2:
        dice_state[0] = 5-dice_state[2]
        dice_state[2] = temp
    elif mv == 3:
        dice_state[0] = dice_state[1]
        dice_state[1] = 5-temp
    elif mv == 4:
        dice_state[0] = 5-dice_state[1]
        dice_state[1] = temp
        
    #change dice_value
    if MAP[nx][ny]==0:
        MAP[nx][ny] = dice_value[dice_state[0]]
    else:
        dice_value[dice_state[0]] = MAP[nx][ny]
        MAP[nx][ny] = 0
    #change dice_xy
    dice_x, dice_y = nx, ny
    
    #print
    print(dice_value[5-dice_state[0]])