def solution(n):
    if n < 2:
        return 0
    
    # 0과 1은 소수가 아니므로 False로 시작
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    # 제곱근까지 배수 제거
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return sum(is_prime)
