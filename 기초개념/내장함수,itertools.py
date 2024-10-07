a = [1,4,3]
print(f"기본 리스트 : {a}")

a.append(2)
print(f"삽입 : {a}")

a.sort()
print(f"오름차순 정렬 : {a}")

a.sort(reverse=True)
print(f"내림차순 정렬 : {a}")

a.reverse()
print(f"원소 뒤집기 : {a}")

a.insert(2,3)
print(f"인덱스 2에 3추가 : {a}")

print(f"값이 3인 데이터개수 : {a.count(3)}")

a.remove(1)
print(f"값이 1인 데이터 삭제 : {a}")

# append 시간 복잡도는 O(1)
# insert append보다 느림
# remove insert와 동일 따라서 남발하면 실행 시간이 느려짐

a = [1,2,3,4,5,5,5]
remove_set = [3,5]

# remove_set에 포함되지 않는 값만 저장
result = [i for i in a if i not in remove_set]
print(result)

# (2) itertools
# 반복되는 데이터 처리에 유용, 대표적으로 permutations, combinations

#모든 순열 구하기 permutations iterable객체에서 n개를 뽑아 일렬로 나열하는 모든 경우를 계산해줌.
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data,3))
print(result)

# combinations iterable객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우
from itertools import combinations

result = list(combinations(data,2))
print(result)

# product
# permutations와 같이 iterable객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든경우를 계산해준다.
# permutations와 다르게 중복을 허용한다.
from itertools import product

result = list(product(data, repeat=2))
print(result)

# combinations_with_replacement
# combination처럼 iterable객체에서 r새의 데이터를 뽑아 순서를 고려하지않고 나열하는 모든 경웅의 수를 계산
# combinations과 다르게 중복을 허용한다.
from itertools import combinations_with_replacement

result = list(combinations_with_replacement(data,2))
print(result)

