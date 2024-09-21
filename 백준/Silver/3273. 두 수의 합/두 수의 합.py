n = int(input())
arr = list(map(int, input().split()))
x = int(input())

def count_pairs_with_sum(arr, x):
    # 집합으로 접근하기
    seen = set()
    count = 0
    
    # 배열의 모든 원소에 대해 반복
    for num in arr:
        # x에서 현재 숫자를 뺀 값이 이미 집합에 있는지 확인
        if x - num in seen:
            count += 1
        seen.add(num)
    
    return count

print(count_pairs_with_sum(arr, x))
