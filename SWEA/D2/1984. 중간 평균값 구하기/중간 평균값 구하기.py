N = int(input())

for testcase in range(1, N+1):
  arr = list(map(int, input().split()))
  arr.remove(max(arr))
  arr.remove(min(arr))
  print(f'#{testcase}', round(sum(arr)/len(arr)))