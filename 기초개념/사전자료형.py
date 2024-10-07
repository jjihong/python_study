# (1) 사전 자료형은 키와 값의 쌍으로 데이터를 이룬다.
# 리스트나 튜플은 순차적으로 저장
# 사전처럼 단어 뜻 연결됨

data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'

print(data)

# 실제로 사전처럼 사용가능
if '사과' in data:
    print("사과를 키값으로하는 데이터가 존재합니다.")

# (2) 사전 자료형 관련 함수
# 키 데이터만 담은 리스트
key_list = data.keys()
# 값 데이터만 담은 리스트
values_list = data.values()
print(key_list)
print(values_list)

# 각 키에 따른 값을 하나씩 출력
for key in key_list:
    print(data[key])

