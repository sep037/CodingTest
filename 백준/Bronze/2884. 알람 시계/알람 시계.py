import sys

input = sys.stdin.readline
a,b = map(int, input().split())

if a!=0:
  if b>=45:
    print(a,b-45)
  else:
    print(a-1,60-45+b)
else:
  if b>=45:
    print(a,b-45)
  else:
    print(23,60-45+b)