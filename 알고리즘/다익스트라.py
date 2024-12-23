# 다익스트라 알고리즘(Dijkstra's Algorithm)
# 가중치가 있는 그래프에서 한 노드에서 다른 모든 노드까지의 최단 경로를 찾는 알고리즘입니다.

# 파이썬 코드 예제

import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # 초기 거리 무한대로 설정
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (distances[start], start))

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if distances[current_node] < current_distance:
            continue  # 이미 처리된 노드 무시

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))
    return distances


# 사용 예시
graph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}
distances = dijkstra(graph, 'A')
print("\n각 노드까지의 최단 거리:")
for node, distance in distances.items():
    print(f"A에서 {node}까지의 거리: {distance}")

# 각 노드까지의 최단 거리:
# A에서 A까지의 거리: 0
# A에서 B까지의 거리: 6
# A에서 C까지의 거리: 1
# A에서 D까지의 거리: 2
# A에서 E까지의 거리: 5
# A에서 F까지의 거리: 6
