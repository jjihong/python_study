# (1) 집합자료형 소개
# 중복을 허용하지 않는다.
# 순서가 없다.

# 집합자료형 초기화 방법 1
data = set([1,1,2,3,4,4,5])
print(data)
# 집합자료형 초기화 방법 2
data = {1,1,2,3,4,4,5}
print(data)

# (2) 집합 자료형의 연산
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])

print(a|b) # 합집합
print(a&b) # 교집합
print(a-b) # 차집합

# (3) 집합 자료형 관련 함수
# 시간복잡도가 모두 O(1)이다.
data = set([1,2,3])

data.add(4)
print(data)

data.update([5,6]) # 여러개를 추가하고 싶을 때
print(data)

data.remove(3)
print(data)