def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif (arr[mid] < target):
            left = mid + 1
        else:
            right = mid - 1
    return 0


# 사용자로부터 입력 받기
n = int(input())

arr = list(map(int, input().split()))

m = int(input())

arr2 = list(map(int, input().split()))

arr.sort()

for i in arr2:
    print(binary_search(arr, i))
