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

