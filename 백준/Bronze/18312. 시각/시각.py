import sys

a, b = map(int, input().split())

count = 0
for i in range(0, a+1):
    if i < 10:
        i = '0' + str(i)
    for j in range(0, 60):
        if j < 10:
            j = '0' + str(j)
        for m in range(0, 60):
            if m < 10:
                m = '0' + str(m)
            if str(b) in (str(i) + str(j) + str(m)):
                count += 1

print(count)