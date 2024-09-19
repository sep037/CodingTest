# def find_closest_to_zero_with_dict(acids, alkalis):
#     result_dict = {}  # 딕셔너리 생성
    
#     for acid in acids:
#         for alkali in alkalis:
#             current_sum = acid + alkali
#             result_dict[(acid, alkali)] = current_sum  # (산성, 알칼리) -> 합
    
#     # 0에 가장 가까운 값 찾기
#     closest_pair = min(result_dict, key=lambda x: abs(result_dict[x]))  # 편차가 가장 작은 쌍 찾기
    
#     return closest_pair, result_dict[closest_pair]


# N = int(input())
# acids = []
# alkalis = []

# for _ in range(N):
#     i = int(input())
#     if i < 0:
#         alkalis.append(i)
#     else:
#         acids.append(i)

# result_pair, result_sum = find_closest_to_zero_with_dict(acids, alkalis)
# print(f"Closest pair: {result_pair[0]}, {result_pair[1]} with sum: {result_sum}")

# 이거 런타임 에러 ! ㅠ

n = int(input())
arr = list(map(int, input().split(' ')))
arr.sort()

left = 0
right = n-1

answer = abs(arr[left] + arr[right])
final = [arr[left], arr[right]]


while left < right:
    left_val = arr[left]
    right_val = arr[right]

    sum = left_val + right_val
  
    if abs(sum) < answer:
        answer = abs(sum)
        final = [left_val, right_val]
        if answer == 0:
          break
    if sum < 0:
        left += 1
    else:
        right -= 1

print(final[0], final[1])