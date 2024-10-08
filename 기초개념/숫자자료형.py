# 정수형

a = 1000
print(a)

a = -7
print(a)

# 0
a = 0
print(a)


# 실수형

# 양의 정수
a = 157.93
print(a)

# 음의 정수
a = -1837.2
print(a)

# 소수부가 0일 때 0을 생략
a = 5.
print(a)

# 정수부가 0일 떄 0을 생략
a = -0.7
print(a)

# 지수 표현 방식 e는 10의 제곱수를 표현
# e1 >> 10의 1제곱 , e5 >> 10의 5제곱 , e-3 >> 10의 -3제곱
a = 1e9
print(a) # 10억

a = 75.25e1
print(a)

a = 3954e-3
print(a)

# 실수의 나눗셈은 정확하지 않다.
# 십진수 체계에서 0.3+0.6은 0.9진수이나,
# 컴퓨터로 0.3+0.6은 0.899999999999이다.
# if (0.3+0.6 == 0.9) 를 계산시 false출력
# 따라서 round()함수를 통해 비교나 계산을 해야한다.

a = 0.3 + 0.6

if round(a, 4) == 0.9: # round 함수를 통해 True 출력을 볼 수 있음.
    print(True)
else:
    print(False)

# 수 자료형의 연산은 +,-,*,/,%(나머지),//(몫),**(거듭제곱) 등이 있으며
# / 나누기는 실수로 처리해야하기 때문에 몫만 얻고자하면 //을 이용하자. (예제 패스)


