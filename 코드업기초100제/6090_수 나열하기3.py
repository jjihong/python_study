# 수 나열하기3
# https://codeup.kr/problem.php?id=6090
a,m,d,n = map(int,input().split())
for i in range(1,n):
    a = a*m+d
print(a)