
fac = int(input())
ramen = list(map(int, input().split()))
money = 0

for i in range(len(ramen)-2):
    if (ramen[i] > 0 and ramen[i+1] > 0 and ramen[i+2] > 0):
        min_count = min(ramen[i], ramen[i+1], ramen[i+2])
        ramen[i] -= min_count
        ramen[i+1] -= min_count
        ramen[i+2] -= min_count
        money += min_count * 7

for i in range(len(ramen)-1):
    if (ramen[i] > 0 and ramen[i+1] > 0):
        min_count = min(ramen[i], ramen[i+1])
        money += min_count * 5
        ramen[i] -= min_count
        ramen[i+1] -= min_count

count2 = 0
for i in range(len(ramen)):
    count2 += ramen[i]

money += 3 * count2
print(money)
