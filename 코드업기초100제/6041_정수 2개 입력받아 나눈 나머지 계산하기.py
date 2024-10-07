# https://codeup.kr/problem.php?id=6041
# 6041 : [기초-산술연산] 정수 2개 입력받아 나눈 나머지 계산하기(설명)(py)
a ,b = map(int,input().split())
print(f"{a%b}")

# print(f"{(lambda a, b: a % b)(*map(int, input().split()))}")
