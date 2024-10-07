# 6059_비트단위로 NOT 하여 출력하기,py
# https://codeup.kr/problem.php?id=6059
#이러한 내용을 간단히 표현하면, 정수 n이라고 할 때,

# ~n = -n - 1
# -n = ~n + 1 과 같은 관계로 표현할 수 있다.

# 입력을 받는다
number = int(input())

# 비트 단위로 반전시킨다
bitwise_not = ~number

# 결과를 출력한다
print(bitwise_not)
