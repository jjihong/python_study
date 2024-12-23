a = [1, 4, 3]
print(f"기본 리스트 : {a}")

a.append(2)
print(f"삽입 : {a}")

a.sort()
print(f"오름차순 정렬 : {a}")

a.sort(reverse=True)
print(f"내림차순 정렬 : {a}")

a.reverse()
print(f"원소 뒤집기 : {a}")

a.insert(2, 3)
print(f"인덱스 2에 3추가 : {a}")

print(f"값이 3인 데이터개수 : {a.count(3)}")

a.remove(1)
print(f"값이 1인 데이터 삭제 : {a}")  # 여러 개면 하나만 삭제(앞에 있는 순)

# append 시간 복잡도는 O(1)
# insert는 O(N)
# insert append보다 느림
# remove insert와 동일 따라서 남발하면 실행 시간이 느려짐

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = [3, 5]

# remove_set에 포함되지 않는 값만 저장
result = [i for i in a if i not in remove_set]
print(result)
