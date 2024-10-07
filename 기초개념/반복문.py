# while

i = 1
result = 0

while i <= 9:
    result += i
    i += 1

print(result)  # 45

# for
'''
    for 변수 in 리스트:
'''
result = 0
for i in range(1, 10):
    result += i

print(result)

scores = [90,85,77,65,97]
for i in range(len(scores)):
    if scores[i] >= 80:
        print(f"{i+1}번 학생은 합격입니다.")

# continue 를 만나면 반복문의 처음으로 돌아감.
scores = [90,85,77,65,97]
cheating_list = {2,4}
for i in range(5):
        if i + 1 in cheating_list:
            continue
        if scores[i] >= 80:
            print(f"{i+1}번 학생은 합격입니다.")

# 구구단 중첩 for문
for i in range(2,10):
    for j in range(1,10):
        print(f"{i} X {j} = {i * j}")
    print()










