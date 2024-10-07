# 정수 3개 입력받아 짝수만 출력하기

a = list(map(int,input().split()))
print(a)
for i in range(3):
    if a[i] % 2 == 0:
        print(a[i])
    else:
        pass
