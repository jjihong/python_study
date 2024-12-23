# 분할 정복 알고리즘의 하나로, 리스트를 반으로 나누어 각각을 정렬한 후 합치는 방식입니다.

# 리스트를 절반으로 나눕니다.
# 나눠진 리스트를 재귀적으로 병합 정렬합니다.
# 두 개의 정렬된 리스트를 병합합니다.
# 모든 경우에 대해 O(n log n)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # 좌우 분할 재귀 호출
        merge_sort(L)
        merge_sort(R)

        # 병합 과정
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # 남은 요소 처리
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# 사용 예시
data = [38, 27, 43, 3, 9, 82, 10]
merge_sort(data)
print(data)  # [3, 9, 10, 27, 38, 43, 82]
