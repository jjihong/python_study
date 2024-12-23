# 선형 탐색 (Linear Search)
# 리스트의 요소를 처음부터 끝까지 순차적으로 탐색하는 방법.
# 최악, 평균의 경우 O(n)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # 인덱스 반환
    return -1  # 찾지 못한 경우


# 사용 예시
data = [5, 3, 8, 4, 2]
index = linear_search(data, 4)
if index != -1:
    print(f"원소 4는 인덱스 {index}에 있습니다.")
else:
    print("원소를 찾을 수 없습니다.")
#  원소 4는 인덱스 3에 있습니다.
