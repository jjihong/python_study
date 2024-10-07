# https://www.acmicpc.net/problem/11399

people_number = int(input())
people_time = list(map(int,input().split()))
result_time = 0
people_time.sort()
for i in range(people_number):
    for j in range(i+1):
        result_time += people_time[j]
print(result_time)
