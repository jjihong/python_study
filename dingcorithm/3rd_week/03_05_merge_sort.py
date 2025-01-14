def merge_sort(array):
    mid = (0 + len(array)) // 2
    left_array = merge_sort(array[:mid]) # 재귀 함수이기때문에 끝꺼자 쪼갤 거임
    right_array = merge_sort(array[mid:])
    merge(left_array, right_array)

def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0

    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    while array1_index < len(array1):
        result.append(array1[array1_index])
        array1_index += 1

    while array2_index < len(array2):
        result.append(array2[array2_index])
        array2_index += 1

    return result

# merge함수의 시간복잡도 O(N) 어레이 index만큼 세기 때문
# merge_sort O(N) x , 병합때문에 N만큼의 연산은 LogN반만큼 해서 O(NlogN)