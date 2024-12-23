# 피벗(pivot)을 기준으로 리스트를 분할하여 정렬하는 분할 정복 알고리즘입니다.

# 리스트에서 피벗을 선택합니다.
# 피벗보다 작은 요소들은 왼쪽 파티션에, 큰 요소들은 오른쪽 파티션에 둡니다.
# 각 파티션에 대해 재귀적으로 퀵 정렬을 수행합니다.

# 평균의 경우 O(n log n)
# 최악의 경우(정렬된 리스트에서 피벗을 최솟값 또는 최댓값으로 선택할 경우) O(n²)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # 피벗 선택
        less = [x for x in arr[1:] if x <= pivot]  # 피벗보다 작은 요소
        greater = [x for x in arr[1:] if x > pivot]  # 피벗보다 큰 요소
        return quick_sort(less) + [pivot] + quick_sort(greater)


# 사용 예시
data = [10, 7, 8, 9, 1, 5]
sorted_data = quick_sort(data)
print(sorted_data)  # [1, 5, 7, 8, 9, 10]
