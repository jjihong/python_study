x = 15
if x>10:
    print(x)

'''
    if 조건문 1 :
        조건문 1이 True일 때 실행되는 코드
    elif 조건문 2 :
        조건문 2이 True일 때 실행되는 코드
    else:
        조건문 1,2,---,n이 모두 True가 아닐 때 실행되는 코드
    
    들여쓰기를 잘 할 것 공백 4칸 = tab
'''

score = 85
if score >= 70:
    print('성적이 우수합니다.')
    if score >= 90:
        print('아주 우수합니다.')
else:
    print("성적이 70점 미만입니다. \n 좀 더 분발하세요.")

print("프로그램 종료")

# 비교 연산자 == , != , > , < , >= , <=
# 논리 연산자 and or not
# x in 리스트 >> 리스트안에 x가 들어있으면 True
# x not in  문자열 >> 문자열안에 x가 들어있지 않으면 True

# 아무것도 하기 싫을때 쓰는 코드
# 디버깅 필요할 때 pass에 빨콩찍고 디버깅 돌림.
# 혹은 나중에 작업할것을 명시
pass

# 한줄 코드 사용시 조건문 한 줄 사용
if score >= 80: result = "Success"
else: result = "Fail"
print(result)

# 조건부 표현식
result = "Success" if score >= 80 else "Fail"
print(result)

# 리스트에서 특정한 원소값을 없앨 때 조건부 활용식의 활용

# 활용 x
a = [1,2,3,4,5,5,5]
remove_set = {3,5}

result = []
for i in a:
    if i not in remove_set:
        result.append(i)

print(result)

# 활용
a = [1,2,3,4,5,5,5]
remove_set = {3,5}

result = [i for i in a if i not in remove_set]
print(result)