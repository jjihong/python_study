# (2) heapq
# heap기능을 사용하기 위해 제공
# 다익스트라 최단경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐를 구현할 때 사용

# heapq외에도 PriorityQueue를 사용할 수 있으나, 느림.
# 파이썬의 힙은 최소 힙으로 구성되어 있어서 단순이 원소를 힙에 전부 넣었다가 빼는 거만으로
# 시간 복잡도 O(NlogN)에 오름차순 정렬이 완료된다.
# 보통 최소 힙 자료구조의 최상단 원소는 가장작은 원소이기 때문

# 원소를 삽입할땐, heapq.heappush()
# 원소를 꺼낼 떄는 heapq.heappop()
# heap 정렬을 heapq로 구현할 때는 다음 예제를 보자.

import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# 파이썬은 최대힙을 제공하지 않는다.
# 따라서 최대 힙을 구현해야할때는 원소의 부호를 임시로 변경하는 방식을 사용한다.

def heapsort2(iterable):
    h = []
    result = []
    #모든원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,-value)
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort2([1,3,5,7,9,2,4,6,8,0])
print(result)








