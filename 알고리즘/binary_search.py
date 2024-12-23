# 정렬된 리스트에서 중간 값을 기준으로 탐색 범위를 반으로 줄여가며 찾는 방법입니다.

# 리스트의 중간 요소를 선택합니다.
# 중간 요소가 찾는 값과 같으면 탐색 종료.
# 찾는 값이 중간 요소보다 작으면 왼쪽 부분 리스트에서 탐색.
# 찾는 값이 중간 요소보다 크면 오른쪽 부분 리스트에서 탐색.
# 이 과정을 반복합니다.
# 모든 경우에 대해 O(log n)

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # 인덱스 반환
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # 찾지 못한 경우


# 사용 예시
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = binary_search(data, 6)
if index != -1:
    print(f"원소 6은 인덱스 {index}에 있습니다.")
else:
    print("원소를 찾을 수 없습니다.")

# 원소 6은 인덱스 5에 있습니다.
