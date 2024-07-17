
N = int(input())
price = []
for _ in range(N):
    price.append(int(input()))
price.sort(reverse=True)

total = 0


for i in range(0, N, 3):
    if i + 2 < N:
        total += price[i] + price[i + 1]
    else:
        total += sum(price[i:N])

print(total)
