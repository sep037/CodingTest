k = int(input())
a, b, c, d = list(map(int, input().split()))

result1 = a*k + b
result2 = c*k + d

if result1 == result2:
    print("Yes",result1)
else:
    print("No")