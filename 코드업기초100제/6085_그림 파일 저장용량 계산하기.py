# 그림 파일 저장용량 계산하기
# https://codeup.kr/problem.php?id=6085

w,h,b=map(float,input().split())
print(f"{(w*h*b/8/1024/1024):.2f} MB")