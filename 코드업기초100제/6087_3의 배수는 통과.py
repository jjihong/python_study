# 3의 배수는 통과
# https://codeup.kr/problem.php?id=6087
a = int(input())
for i in range(a+1):
    if i % 3 == 0:
        continue
    else:
        print(i, end=" ")