# 짝수 합 구하기
a = int(input())
result = 0
while a >= 0 :
    if a % 2 == 0:
        result += a
    a -= 1
print(f"{result}")