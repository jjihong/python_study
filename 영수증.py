tot = int(input())
count = int(input())

for i in range(count):
    a, b = map(int, input().split())
    tot -= a * b

print("Yes") if tot == 0 else print('No')
