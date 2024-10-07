# 소리 파일 저장용량 계산하기
# https://codeup.kr/problem.php?id=6084

h,b,c,s=map(float,input().split())
print(f"{round((h*b*c*s/8/1024/1024),1)} MB")