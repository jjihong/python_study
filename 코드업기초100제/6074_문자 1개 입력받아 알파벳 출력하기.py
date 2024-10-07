# 문자 1개 입력받아 알파벳 출력하기
# https://codeup.kr/problem.php?id=6074
a = ord(input())
s = 97
while s <= a:
    print(f"{chr(s)}",end=" ")
    s += 1