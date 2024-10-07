# 표준 라이브러리란 특정 프로그래밍언어에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리.
# docs.python.org/ko/3/library/index.html
'''
내장 함수
itertools 반복되는 형태의 데이터 처리 , 순열과 조합
heapq: heap기능을 제공, 우선순위 큐 구현시 사용
bisect : 이진 탐색기능을 제공하는 라이브러리
collections: deque, counter등의 유용한 자료구조를 포함하는 라이브러리
'''
# (1) 내장 함수 > 별도 import가 필요없음
# iterable객체 > 반복 가능한 객체 즉, 리스트,튜플,사전,세트
# input,print,sum(iterable객체),max(),min(),
# eval()>수학수식을 문자열로 입력시 계산
# sorted() 정렬된 결과를 반환
result = sorted([9,1,8,5,4])
print(result)
result = sorted([9,1,8,5,4], reverse=True)
print(result)
# 그러나 iterable객체는 기본으로 sort()함수를 내장하고 있다.


