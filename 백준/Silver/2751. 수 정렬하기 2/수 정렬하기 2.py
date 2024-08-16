import sys

input = sys.stdin.readline
n = int(input())
list = []

for i in range(n):
  list.append(int(input()))
  
for i in sorted(list): # sorted는 원배열까지 영향을 미치지 않는다
  print(i)