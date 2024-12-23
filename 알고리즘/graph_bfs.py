# 너비 우선 탐색(BFS, Breadth-First Search)
# 큐를 사용하여 그래프의 노드를 넓게 탐색하는 방법입니다.
from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# 사용 예시
print("\nBFS 방문 순서:")
bfs(graph, 'A')
# BFS 방문 순서:
# A B C D G H I E F J
