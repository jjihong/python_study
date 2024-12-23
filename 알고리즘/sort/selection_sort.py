# 리스트에서 가장 작은 요소를 찾아 맨 앞의 요소와 교환하는 방식으로 정렬합니다.

# 리스트에서 최소값을 찾습니다.
# 최소값을 리스트의 첫 번째 요소와 교환합니다.
# 나머지 리스트에 대해 이 과정을 반복합니다.
# 최악, 평균, 최선의 경우 모두 O(n²)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        # 나머지 요소 중 최소값 찾기
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 최소값을 맨 앞의 요소와 교환
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# 사용 예시
data = [64, 25, 12, 22, 11]
selection_sort(data)
print(data)  # [11, 12, 22, 25, 64]

