# 그래프 구조에서의 문제를 해결하기 위한 알고리즘입니다.

# 3.8.1 깊이 우선 탐색(DFS, Depth-First Search)
# 재귀나 스택을 사용하여 그래프의 노드를 깊게 탐색하는 방법입니다.

def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=' ')
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# 사용 예시
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'G', 'H', 'I'],
    'D': ['B', 'E', 'F'],
    'E': ['D'],
    'F': ['D'],
    'G': ['C'],
    'H': ['C'],
    'I': ['C', 'J'],
    'J': ['I']
}
visited = set()
print("DFS 방문 순서:")
dfs(graph, 'A', visited)
# DFS 방문 순서:
# A B D E F C G H I J
