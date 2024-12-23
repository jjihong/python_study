# 반복되는 데이터 처리에 유용, 대표적으로 permutations, combinations

from itertools import combinations_with_replacement
from itertools import product
from itertools import combinations
from itertools import permutations

# from itertools import permutaions
# 모든 순열 구하기 permutations iterable객체에서 n개를 뽑아 일렬로 나열하는 모든 경우를 계산해줌.
# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]
data = ['A', 'B', 'C']

result = list(permutations(data, 3))
print(result)

# combinations iterable객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우
# from itertools import combinations
# [('A', 'B'), ('A', 'C'), ('B', 'C')]
result = list(combinations(data, 2))
print(result)

# product
# from itertools import product
# permutations와 같이 iterable객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든경우를 계산해준다.
# permutations와 다르게 중복을 허용한다.
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
result = list(product(data, repeat=2))
print(result)

# combinations_with_replacement
# combination처럼 iterable객체에서 r새의 데이터를 뽑아 순서를 고려하지않고 나열하는 모든 경웅의 수를 계산
# combinations과 다르게 중복을 허용한다.
# from itertools import combinations_with_replacement
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

result = list(combinations_with_replacement(data, 2))
print(result)
