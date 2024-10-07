# 정수 3개 입력받아 가장 작은 값 출력하기

a,b,c = map(int,input().split())
print(f"{a if a<b and a<c else b if a>b and b<c else c}")