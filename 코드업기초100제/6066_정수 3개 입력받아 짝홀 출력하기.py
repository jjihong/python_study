# 정수 3개 입력받아 짝/홀 출력하기
a = list(map(int,input().split()))
for i in range(3):
    if a[i] % 2 == 0:
        print("even")
    else:
        print("odd")
