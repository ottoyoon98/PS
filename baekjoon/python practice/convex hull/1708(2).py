import sys
import math
input = sys.stdin.readline

def CCW(P1, P2, P3):
    return (P2[0]-P1[0])*(P3[1]-P1[1])-(P2[1]-P1[1])*(P3[0]-P1[0])

def main():
    n = int(input())
    Point = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda P: (P[0],P[1]))
    for i in range(n):
        x, y = Point[i][0]-Point[0][0], Point[i][1]-Point[0][1]
        length = math.sqrt(x**2+y**2)
        x, y = (x/length, y/length) if length != 0 else (0, 0)
        Point[i] += [x, y]
    BP = Point[1][2:4]
    Point = [Point[0]] + sorted(Point[1:], key=lambda P: (CCW([0,0], BP, P[2:4]),(P[0]**2+P[1]**2))) + [Point[0]]

    stack = [Point[0][0:2], Point[1][0:2]]
    top = 1
    for i in range(2, n+1):
        next = Point[i][0:2]
        while True:
            second = stack[top]
            first = stack[top-1]
            ccw=CCW(first, second, next)
            if ccw>0 or top==0:
                stack.append(next)
                top += 1
                break
            elif ccw <= 0:
                stack.pop()
                top -= 1
    print(top)
    return 0

if __name__ == "__main__":
    main()
