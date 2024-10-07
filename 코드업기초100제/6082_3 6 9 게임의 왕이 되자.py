# 3 6 9 게임의 왕이 되자
# https://codeup.kr/problem.php?id=6082
n = int(input())
for i in range(1, n+1) :
  if i % 10 in [3,6,9] or i // 10 in [3,6,9] :
    print("X", end=' ')    #출력 후 공백문자(빈칸, ' ')로 끝냄
  else:
    print(f"{i}" ,end=' ')
