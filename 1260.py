# 1 - 2 3 4
# 2 - 4
# 3 - 4
# 1 > 2 > 3 > 4
#
# 5 5 3
# 1 - 2
# 3 - 1 4
# 5 - 2 4
#
# 3 - 1 - 4 - 2 - 5

from collections import deque

def bfs (adjacent_graph, start_node):
    for node in graph:
        graph[node].sort()

    queue = deque([start_node])
    visited = []
    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            visited.append(current_node)

        for adjacent_node in adjacent_graph[current_node]:
            if adjacent_node not in visited:
                queue.append(adjacent_node)

    return visited


def dfs(adjacent_graph, start_node):
    for node in graph:
        graph[node].sort(reverse=True)

    stack = [start_node]
    visited = []
    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.append(current_node)

        for adjacent_node in adjacent_graph[current_node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)
    return visited

n, m, v = map(int,input().split())

#인접 리스트 초기화
graph = { i: [] for i in range(1, n+1) }

for _ in range(m):
    s, g = map(int, input().split())
    graph[s].append(g)
    graph[g].append(s)

a , b = dfs(graph,v) , bfs(graph, v)
for item in a:
    print( item , end = ' ')
print()
for item in b:
    print( item , end = ' ')

