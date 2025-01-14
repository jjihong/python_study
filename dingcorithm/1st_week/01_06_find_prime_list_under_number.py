input = 20

# 소수는 자기자신과 1외에는 아무것도 나눌 수 없다.
def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    prime_list = []
    # 2~20까지 소수면 prime list에 넣자
    for n in range(2, number + 1):
        for i in range(2, n):
            if n % i == 0:
                break
        else: prime_list.append(n)
    return prime_list

result = find_prime_list_under_number(input)
print(result)