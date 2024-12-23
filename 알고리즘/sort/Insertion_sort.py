# 정렬된 부분에 새로운 요소를 알맞은 위치에 삽입하여 정렬하는 방식입니다.

# 두 번째 요소부터 시작하여 현재 요소를 앞의 정렬된 부분과 비교합니다.
# 현재 요소보다 큰 요소들은 한 칸씩 뒤로 밀립니다.
# 현재 요소를 알맞은 위치에 삽입합니다.
# 리스트의 끝까지 이 과정을 반복합니다.
# https://gmlwjd9405.github.io/2018/05/06/algorithm-insertion-sort.html
# 최악, 평균의 경우 O(n²)
# 최선의 경우(이미 정렬된 경우) O(n)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # key보다 큰 요소들은 한 칸씩 뒤로 이동
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # key를 알맞은 위치에 삽입
        arr[j + 1] = key


# 사용 예시
data = [12, 11, 13, 5, 6]
insertion_sort(data)
print(data)  # [5, 6, 11, 12, 13]
