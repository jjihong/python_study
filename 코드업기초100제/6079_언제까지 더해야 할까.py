# 언제까지 더해야 할까?
# https://codeup.kr/problem.php?id=6079
result = 0
a = int(input())
for i in range (a):
    result += i
    if result >= a:
        print(i)
        break