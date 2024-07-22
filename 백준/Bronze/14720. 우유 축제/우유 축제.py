N = int(input())

k = list(map(int, input().split()))

count = 0
for i in range(N):
  if k[i] == count%3:
    count += 1
    
print(count)