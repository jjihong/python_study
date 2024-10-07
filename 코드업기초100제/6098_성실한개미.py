# 바둑판 상태를 입력받아 초기화
board = [[0 for _ in range(10)] for _ in range(10)]

for i in range(10):
    row = list(map(int, input().split()))
    for j in range(10):
        board[i][j] = row[j]
find = 0
x, y = 1, 1
while True:

    board[x][y] = 9
    if find == 2:
        break

    if board[x][y + 1] == 0:
        y += 1
        continue
    elif board[x][y + 1] == 2:
            find = 2
            y += 1
            continue
    elif board[x][y + 1] == 1:
        if board[x + 1][y] == 0:
            x += 1
            continue
        elif board[x + 1][y] == 1 or board[x+1][y] == 2:
            find = 2
            if x != 8: x+=1
            continue

for i in range(10):
    for j in range(10):
        print(f"{board[i][j]}", end=" ")
    print()
