# 6055 : [기초-논리연산] 하나라도 참이면 참 출력하기(설명)(py)
# https://codeup.kr/problem.php?id=6055
a,b = map(int,input().split())
print(f"{bool(a or b)}")
