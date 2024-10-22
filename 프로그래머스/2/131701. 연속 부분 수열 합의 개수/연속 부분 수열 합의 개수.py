def solution(elements):
    n = len(elements)
    elements = elements * 2  # 원형 수열을 처리하기 위해 두 번 이어 붙임
    sums = set()  # 가능한 모든 연속 부분 수열의 합을 저장할 집합

    # 길이 1부터 n까지의 부분 수열 합을 구함
    for length in range(1, n + 1):
        for start in range(n):
            sums.add(sum(elements[start:start + length]))

    return len(sums)
