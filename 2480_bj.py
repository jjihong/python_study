a = []
a = input()
b = sorted(a.split())  # 입력받은 숫자를 공백으로 쪼개서 정렬함.
result = 0

if b[0] == b[1] == b[2]:
    result = 10000 + int(b[0]) * 1000
elif (b[0] != b[2]):
    if (b[1] == b[0] or b[1] == b[2]):
        result = 1000 + int(b[1]) * 100
    else:
        result = int(b[2]) * 100
elif (b[0] == b[2] and (b[0] != b[1] and b[1] != b[2])):
    result = int(b[2]) * 100

print(result)
