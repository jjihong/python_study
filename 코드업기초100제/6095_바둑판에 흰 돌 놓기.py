a = [[0 for _ in range(19)] for _ in range(19)]

b = int(input())

for i in range(b):
    c,d = map(int,input().split())
    a[c-1][d-1] = 1

for i in range(19):
    for j in range(19):
        print(f"{a[i][j]}",end=" ")
    print()