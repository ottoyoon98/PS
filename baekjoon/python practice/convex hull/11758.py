def CCW(P1, P2, P3):
    ccw = (P2[0]-P1[0])*(P3[1]-P1[1])-(P3[0]-P1[0])*(P2[1]-P1[1])
    return 0 if ccw==0 else (1 if ccw>0 else -1)


P1 = list(map(int, input().split()))
P2 = list(map(int, input().split()))
P3 = list(map(int, input().split()))

print(CCW(P1, P2, P3))
