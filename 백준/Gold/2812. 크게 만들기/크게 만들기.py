N, M = map(int, input().split())
num = input()

result = []
remove_count = M

for digit in num:
    while remove_count > 0 and result and result[-1] < digit:
        result.pop()
        remove_count -= 1
    result.append(digit)

result = result[:N-M]
print(''.join(result))
