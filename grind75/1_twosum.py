def two_sum(nums, target):
    # 숫자와 인덱스를 저장할 딕셔너리 생성
    num_map = {}

    # 배열을 순회하면서
    for i, num in enumerate(nums):
        # target에서 현재 숫자를 뺀 값을 찾음
        complement = target - num

        # 만약 그 값이 딕셔너리에 있으면, 정답을 반환
        if complement in num_map:
            return [num_map[complement], i]

        # 현재 숫자와 인덱스를 딕셔너리에 저장
        num_map[num] = i

    # 항상 하나의 정답이 있다고 문제에서 주어졌으므로, 이 부분은 실행되지 않음
    raise ValueError("No two sum solution")


# 사용자로부터 입력 받기
nums = list(map(int, input("숫자 배열을 입력하세요 (예: 2 7 11 15): ").split()))
target = int(input("타겟 숫자를 입력하세요: "))

# 두 수의 합을 구하고 결과 출력
result = two_sum(nums, target)
print(f"두 수의 인덱스: {result}")
