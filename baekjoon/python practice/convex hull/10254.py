import sys
input = sys.stdin.readline
def main():
    for _ in range(int(input())):
        n = int(input())
        Points = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda p: (p[1], p[0]))
        base = [Points[0], Points[1]]
        print(base)
        print(Points)
        Points = sorted(Points, key=lambda p: ((base[1][0]-base[0][0])*(p[1]-base[0][1])-(p[0]-base[0][0])*(base[1][1]-base[0][1])))
        print(Points)
        for p in Points:
            print(((base[1][0]-base[0][0])*(p[1]-base[0][1])-(p[0]-base[0][0])*(base[1][1]-base[0][1])), end="   ")
        print(base)

    return


if __name__ == "__main__":
    main()