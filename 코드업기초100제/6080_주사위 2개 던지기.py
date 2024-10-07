# 주사위 2개 던지기
# https://codeup.kr/problem.php?id=6080
a, b = map(int, input().split())
for i in range(a):
    for j in range(b):
        print(f"{i+1} {j+1}")
