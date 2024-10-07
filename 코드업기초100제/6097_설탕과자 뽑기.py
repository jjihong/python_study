a,b = map(int,input().split())

# 2차원 리스트 'c'를 0으로 초기화
c = [[0 for _ in range(b)] for _ in range(a)]

d = int(input())
for i in range(d):
    size,direct,x,y = map(int,input().split())
    if direct == 0:
        for j in range(size):
            c[x-1][y-1+j] = 1
    else:
        for j in range(size):
            c[x-1+j][y-1] = 1

for i in range(a):
    for j in range(b):
        print(f"{c[i][j]}", end=" ")
    print()