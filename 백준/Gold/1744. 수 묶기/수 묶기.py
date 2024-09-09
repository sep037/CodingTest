import sys

def max_sum_sequence(arr):
    negative = []
    positive = []
    zero_count = 0
    total_sum = 0

    for num in arr:
        if num < 0:
            negative.append(num)
        elif num > 0:
            positive.append(num)
        else:
            zero_count += 1

    # 음수 정렬 (오름차순)
    negative.sort()
    # 양수 정렬 (내림차순)
    positive.sort(reverse=True)


    while len(negative) > 1:
        total_sum += negative.pop(0) * negative.pop(0)
    if negative:
        total_sum += negative[0] if zero_count == 0 else 0

    while len(positive) > 1:
        a = positive.pop(0)
        b = positive.pop(0)
        if a == 1 or b == 1:
            total_sum += a + b
        else:
            total_sum += a * b
    if positive:
        total_sum += positive[0]

    return total_sum

# 처음에 왜 틀렸는지 봤더니 1은 곱하는 것보다 더하는 게 이득인데 이거 처리 안 함 !
# 완전 바보임


N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))


print(max_sum_sequence(arr))
