# 이상한 출석 번호 부르기2
b = input().split()
c = list(map(int,input().split()))
c.reverse()
for i in range(len(c)): print(f"{c[i]}",end=" ")