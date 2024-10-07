# bisect
# 파이썬은 이진탐색을 쉽게 구현할수있도로 bisect를 제공
# 정렬된 배열 속에서 특정원소를 찾아야 할 때 매우 효과적으로 사용됨.
# bisect_left() , bisect_right()를 함수가 가장 중요하게 이용
# 두 함수의 시간 복잡도는 O(logN)

# bisect_left(a, x) > 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(a, x) > 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
'''
배열이 1 2 4 4 8
이렇게 있을때, 새롭게 데이터 4를 넣으려 한다.
그러면 1 2 (bisect_left) 4 4 (bisect_right) 8
이렇게 정렬을 유지하되 4를 넣을 곳을 왼쪽인지 오른쪽인지 골라 그 인덱스를 찾을 수 있다.
'''

# 이 파일 이름이 원래 bisect.py였는데 이러면 bisect import가 안됨. 유의하자.
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))

# count_by_range(a, left_value, right_value)
# 이는 정렬된 리스트에서 left_value,right_value에 속하는 데이터의 개수를 변환한다.
def count_by_range(a,left_value, right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1,2,3,3,3,3,4,4,8,9]

print(count_by_range(a,4,4)) # 2 > 4,4
print(count_by_range(a,-1,3)) # 6 > 1,2,3,3,3,3

