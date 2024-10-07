# 16진수 구구단 출력하기(py)
# https://codeup.kr/problem.php?id=6081
a = int(input(),16)
for i in range(1,16):
    print(f"{hex(a).upper()[2:]}*{hex(i).upper()[2:]}={hex(a*i).upper()[2:]}")