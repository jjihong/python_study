input = 3


def fibo_recursion(n):
    # 구현해보세요!
    if n == 1 or n == 2:
        return 1

    return fibo_recursion(n-1) + fibo_recursion(n-2)


print(fibo_recursion(input))  # 6765

# 재귀함수로 구현한 피보나치 함수는 매우 비효율적임., 수가 커지면 오래 걸림.
# 동적계획법을 활용!
