S = int(input().strip())
def max_n(S):
    current_sum = 0  # 현재까지의 합
    num = 1
    count = 0  # 개수

    # S보다 합이 작거나 같을 때까지 반복
    while current_sum + num <= S:
        current_sum += num  # 현재 수를 합에 더함
        count += 1
        num += 1  # 다음 자연수

    return count

print(max_n(S))
