'''
def 함수명(매개변수):
    실행할 코드
    return 반환 값 (종료후 값반환)
'''


def add(a, b):
    return a + b


print(add(3, 4))

print(add(b=5, a=4)) # 순서상관없이 직접 지정도 가능

# 함수 안에서 밖에 변수 사용 global
a = 0

def func():
    global a
    a+=1

for i in range(10):
    func()

print(a)

# 람다식
print((lambda a,b: a+b)(3,7))