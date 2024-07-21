# 이거 먼가 확통문제에서 본 것 같음 = 조힙
# m>n이니까 mCn 이거
# m!/(m-n)!*n!

def factorial(e):
  num = 1
  for i in range(1, e+1):
    num *= i
  return num
k = int(input())

matrix = []
for i in range(k):
  n, m = map(int, input().split())
  result = factorial(m) // (factorial(m-n) * factorial(n))
  matrix.append(result)

for i in range(len(matrix)):
  print(matrix[i])