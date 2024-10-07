# collections 라이브러리는 유용한 자료구조를 제공함
# 코테에서는 deque와 Counter가 유용하게 쓰임

# 파이썬은 deque를 이용하여 큐를 구현한다.
# Queue 라이브러리가 있으나 일반적인 큐 자료구조랑 달라서 deque를 쓴다.

# 리스트자료형은 데이터 삽입,삭제 등의 다양한 기능을 제공한다.
# 리스트가 있을 때 중간에 특정한 원소를 삽입하는 것이 가능하다.
# 하지만 리스트 자료형은 append,pop을 할 때, 가장 뒤 쪽 원소를 기준으로 하기 때문에
# 앞쪽에 있는 원소를 처리할 때에는 리스트에 포함된 데이터 개수가 많으면 많은 시간이 소요된다.
#
# 가장 앞쪽에 원소 추가 리: O(N) 데 : O(1)
# 가장 뒤쪽에 원소 추가 리: O(1) 데 : O(1)
# 가장 앞쪽에 원소 제거 리: O(N) 데 : O(1)
# 가장 뒤쪽에 원소 제거 리: O(1) 데 : O(1)
#
# deque에서는 인덱싱,슬라이싱 지원 x
# 나열된 데이터에 양 끝으로 삽입하거나 삭제할 때 효과적
# 스택이나 큐의 기능을 모두 포함하기 때문에 사용
#
# 첫번째 원소 제거 popleft() 끝은 pop()
# 첫번째 인덱스에 삽입 appendleft(x) 끝은 append(x)
# 따라서 deque를 큐로 쓸 때는 삽입 append 제거는 popleft 그럼 FIFO완성

from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)
print(data) # deque([1, 2, 3, 4, 5])
print(list(data)) # [1, 2, 3, 4, 5]

# Counter는 등장 횟수를 세는 기능을 제공
# iterable객체가 주어졌을 때, 객체 내부의 원소가 몇번 씩 등장했는지 알려줌.
# 따라서 원소별 등장 횟수를 세는기능이 필요할 떄 짧은 소스코드로 구현가능
from collections import Counter

counter = Counter(['red','blue','red','green','blue','blue'])
print(counter['blue']) # 3
print(counter['green']) # 1
print(dict(counter)) # {'red': 2, 'blue': 3, 'green': 1}


























