import sys

input = sys.stdin.readline

n = int(input().strip())

coins = [500, 100, 50, 10, 5, 1]

money = 1000 - n
count = 0

for coin in coins:
    money_count = money // coin
    count += money_count
    money -= money_count * coin

print(count)
