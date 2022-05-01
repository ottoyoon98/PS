n = int(input())
consulting = [tuple(map(int, input().split())) for i in range(n)]
D = [0,]*20
j = 0
for i in range(1, n+1):
    t, p = consulting[i-1]
    D[i] = max(D[i], D[i-1])
    if i+t <= n+2:
        D[i+t]=max(D[i+t], D[i]+p)
print(max(D[n], D[n+1]))