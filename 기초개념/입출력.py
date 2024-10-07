# input
# input()함수는 한줄의 문자열을 입력받는다.
# 문자열을 숫자로 받아 정수형으로 쓰려면 int()함수를 사용해야한다.

# 보통 여러 숫자를 받을 때 공백을 스페이스를 넣는데,
# 이를 리스트로 만들 때 list(map(int, input().split()))을 활용함.(외워둘 것)
n = int(input()) # 입력할 갯수
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# n, m, k를 공백으로 입력
n, m, k = map(int, input().split())
print(n,m,k)

# sys.stdin.readline().rstrip()
# rstrip하는 이유는 맨 마지막에 \n 줄바꿈기호인 공백문자를 잘라내기 위함.
# 많은 용량의 인풋이 들어올때 입력의 속도를 아끼기 위한 방법
# import sys 필수

import sys
data = sys.stdin.readline().rstrip()
print(data)

# print는 생략. f-string 개 꿀 f"{a}"