from collections import deque
N, M = map(int, input().split())
board=[]

def BFS():
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue=deque()
    queue.append((R_pos, B_pos, 0))
    while queue:
        R_cpos, B_cpos, clevel = queue.popleft()
        n_level = clevel+1
        if n_level>10:
            continue
        for dx, dy in dirs:
            blue_check = False
            red_check = False
            R_npos = list(R_cpos)
            B_npos = list(B_cpos)
            while board[R_npos[0]+dx][R_npos[1]+dy]!='#' and board[B_npos[0]+dx][B_npos[1]+dy]!='#':
                R_npos= [R_npos[0]+dx, R_npos[1]+dy]
                B_npos= [B_npos[0]+dx, B_npos[1]+dy]
                if tuple(R_npos) == O_pos:
                    red_check = True
                    break
                elif tuple(B_npos) == O_pos:
                    blue_check = True
                    break
            
            if blue_check:
                continue
            
            while board[R_npos[0]+dx][R_npos[1]+dy]!='#' and not red_check:
                R_npos= [R_npos[0]+dx, R_npos[1]+dy]
                if tuple(R_npos) == O_pos:
                    red_check = True
                    break
            
            while board[B_npos[0]+dx][B_npos[1]+dy]!='#' and not blue_check:
                B_npos = [B_npos[0]+dx, B_npos[1]+dy]
                if tuple(B_npos) == O_pos:
                    blue_check = True
                    break
            if blue_check:
                continue
            elif red_check:
                return n_level
            
            if R_npos == B_npos:
                if R_cpos[0] == B_cpos[0] and dx==0:
                    if (R_cpos[1]-B_cpos[1])*dy > 0:
                        B_npos[1]-=dy
                    else:
                        R_npos[1]-=dy
                elif R_cpos[1] == B_cpos[1] and dy==0:                    
                    if (R_cpos[0]-B_cpos[0])*dx > 0:
                        B_npos[0]-=dx
                    else:
                        R_npos[0]-=dx
            if tuple(R_npos)!=R_cpos or tuple(B_npos)!=B_cpos:
                queue.append((tuple(R_npos), tuple(B_npos), n_level))
    return -1


for i in range(N):
    """
    input character 
    '.': Empty space
    '#': Block
    'O': hole
    'R': Red ball
    'B': Blue ball
    """
    board.append(list(input()))
    if 'O' in board[i]:
        O_pos = (i, board[i].index('O'))
    if 'R' in board[i]:
        R_pos = (i, board[i].index('R'))
    if 'B' in board[i]:
        B_pos = (i, board[i].index('B'))

print(BFS())
"""
##########
#B####...#
#R#..#.#.#
#.#....#.#
#.#..O.#.#
#.#.##.#.#
#.#....#.#
#.######.#
#........#
##########
"""