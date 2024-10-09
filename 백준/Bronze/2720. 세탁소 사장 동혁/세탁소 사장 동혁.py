import sys

input = sys.stdin.read
data = input().split()

N = int(data[0])

K = list(map(int, data[1:]))

price = [25, 10, 5, 1]

for i in range(N):
    change = K[i]
    num = [0, 0, 0, 0]
    
    for j in range(4):
        num[j] = change // price[j]
        change %= price[j]
    
    print(*num)
