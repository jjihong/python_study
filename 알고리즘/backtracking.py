# 백트래킹(Backtracking)
# 모든 가능한 경우를 탐색하면서 해가 아닌 경로는 되돌아가는(백트랙) 방식으로 문제를 해결합니다.

# 예제: N-Queen 문제
# N x N 체스판에 N개의 퀸을 서로 공격하지 못하도록 놓는 문제입니다.

def is_safe(queen, row):
    for i in range(row):
        if queen[i] == queen[row] or abs(queen[i] - queen[row]) == row - i:
            return False
    return True


def n_queens(queen, row, n):
    count = 0
    if row == n:
        return 1
    for col in range(n):
        queen[row] = col
        if is_safe(queen, row):
            count += n_queens(queen, row + 1, n)
    return count


# 사용 예시
n = 8
queen = [0] * n
result = n_queens(queen, 0, n)
print(f"{n}퀸 문제의 해의 수:", result)  # 8퀸 문제의 해의 수: 92
