# (1) 리스트 만들기
# 대괄호 안에 원소를 넣어 초기화

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)

print(a[4])  # 인덱스 접근

a = list()  # 빈 리스트 생성 1
print(a)

a = []  # 빈 리스트 생성 2

# 리스트 크기가 N이고 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

# (2) 리스트의 인덱싱과 슬라이싱
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 뒤에서 세기 -를 기준
print(a[-1])

a[3] = 7  # 원소 값 변경
print(a)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 두 번째 원소부터 네 번째 원소 까지
print(a[1:4])

# (3) 리스트 컴프리헨션
# 리스트를 초기화하는 방법

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]

print(array)

# 1부터 9까지의 수의 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10) if i]

print(array)

# 리스트 컴프리헨션은 2차원 리스트를 특정크기로 초기화해야 할 떄 사용함.
# N x M 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)] # _는 반복하되, i의 변수값이 필요없으면 생략해서 쓰는 것
print(array)

# 리스트 컴프리헨션 안쓰면 이 꼴남.
n = 3
m = 4
array = [[0] *m]*n
print(array)

array[1][1] = 5
print(array)
# 내부적으로 포함된 3개의 리스트가 모두 동일한 객체에 대한 3개의 레퍼런스로 인식함.


