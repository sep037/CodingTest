from itertools import combinations

def is_prime(num): #소수게 아니게
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    count = 0
    # nums 배열에서 3개의 숫자 조합 다 구하기
    for trio in combinations(nums, 3):
        if is_prime(sum(trio)):  # 각 조합의 합이 소수인지 확인하기
            count += 1
    return count
