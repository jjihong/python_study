# 동적 프로그래밍(Dynamic Programming)
# 복잡한 문제를 해결하기 위해 작은 하위 문제의 해를 저장하여 재사용하는 방법입니다.
# 메모이제이션(Memoization) 기법을 사용하여 중복 계산을 줄입니다.

# 예제: 피보나치 수열
# 피보나치 수열의 n번째 수를 동적 프로그래밍으로 계산합니다.
# 메모이제이션을 위한 리스트 초기화
memo = {0: 0, 1: 1}


def fib(n):
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


# 사용 예시
n = 9
result = fib(n)
print(f"피보나치 수열의 {n}번째 수:", result)
