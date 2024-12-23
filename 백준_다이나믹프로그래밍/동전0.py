# 입력 받기
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# DP 배열 초기화
dp = [0] * (k + 1)
dp[0] = 1  # 0원을 만들 수 있는 방법은 아무 동전도 사용하지 않는 경우 1가지

# 동전별로 경우의 수 계산
for coin in coins:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]

# 출력
print(dp[k])

#gpt가 품. 다시 볼것