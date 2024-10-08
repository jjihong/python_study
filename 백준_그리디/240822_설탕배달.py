# https://www.acmicpc.net/problem/2839

def sugar_delivery(n):
    count = 0
    while n >= 0:
        if n % 5 == 0:
            count += n // 5
            return count
        n -= 3
        count += 1
    return -1


n = int(input())
print(f"{sugar_delivery(n)}")
