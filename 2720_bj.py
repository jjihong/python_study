tc = int(input())
a = [] 
for i in range(tc):
    a.append(input()) 
# 테스트 케이스 갯수로 for문을 돌려서 리스트로 받기

for i in range(len(a)):
    inputmoney = int(a[i])
    quarter = int(inputmoney / 25)
    inputmoney = inputmoney % 25
    dime = int(inputmoney / 10)
    inputmoney = inputmoney % 10
    nickel = int(inputmoney / 5)
    inputmoney = inputmoney % 5
    penny = int(inputmoney / 1)
    print(quarter, dime, nickel, penny)
# 나누기 연산은 소숫점으로 나오기 떄문에 Int함수를 써야함.