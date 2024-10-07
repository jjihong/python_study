# 거기까지! 이제 그만~
# https://codeup.kr/problem.php?id=6086
a = int(input())
result = 0
for i in range(1,a+1):
    result += i
    if result >= a:
        break
print(result)