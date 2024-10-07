# 19x19 바둑판 초기화
board = [[0 for _ in range(19)] for _ in range(19)]

# 바둑판 상태를 입력받아 초기화
for i in range(19):
    row = list(map(int, input().split()))
    for j in range(19):
        board[i][j] = row[j]

b = int(input())

for i in range(b):
    c,d = map(int,input().split())
    for j in range(19):
        board[c-1][j] = 1 if board[c-1][j] == 0 else 0
    for j in range(19):
        board[j][d-1] = 1 if board[j][d-1] == 0 else 0

for i in range(19):
    for j in range(19):
        print(f"{board[i][j]}",end=" ")
    print()