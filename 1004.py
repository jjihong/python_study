t = int(input())


for i in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    count = 0
    n = int(input())
    for j in range(n):
        c1, c2, r = map(int, input().split())
        d1 = ((c1 - x1) ** 2) + ((c2 - y1) ** 2)
        d2 = ((c1 - x2) ** 2) + ((c2 - y2) ** 2)
        if (d1 <= r ** 2 and d2 >= r ** 2): count +=1
        if (d1 >= r ** 2 and d2 <= r ** 2): count +=1
        print(count)

# 원과 원사이의 거리와, 원의 방정식을 알아야함.