# 분할 정복(Divide and Conquer)
# 문제를 더 작은 하위 문제로 분할하여 각각을 해결한 후,
# 결과를 합쳐서 문제를 해결하는 알고리즘 설계 기법입니다. 병합 정렬과 퀵 정렬이 대표적인 예입니다.

# 예제: 큰 수의 제곱 계산
# 큰 수의 거듭제곱을 효율적으로 계산하는 방법입니다.

def power(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        y = power(x, n // 2)
        return y * y
    else:
        return x * power(x, n - 1)


# 사용 예시
result = power(2, 10)
print(result)  # 1024
