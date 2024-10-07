# 이상한 출석 번호 부르기1
# https://codeup.kr/problem.php?id=6092
a = [0] * 23
b = input().split()
c = list(map(int,input().split()))

for i in range(len(c)):
    if 0 < c[i] < 24:
        a[c[i]-1] += 1
for i in range(len(a)):
    print(a[i],end=" ")