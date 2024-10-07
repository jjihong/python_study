# https://www.acmicpc.net/problem/11047

n, money = map(int,input().split())
coins = []
count = 0
for i in range(n):
    coins.append(int(input()))

coins.reverse()
index = 0

for coin in coins:
    count += money // coin
    money = money % coin


# for i in range(len(coins)):
#     if (coins[i] <= money):
#         if (money % coins[i] == 0):
#             count += money // coins[i]
#             money = 0
#             break
#         elif (money % coins[i] != 0):
#             while(money>coins[i]):
#                 money -= coins[i]
#                 count += 1
#     elif (coins[i] > money):
#         continue

print(f"{count}")