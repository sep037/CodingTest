def solution(n):
    # n이 1 또는 2일 경우 미리 처리 왜냐면 난 피보나치수로 쓸 것이기 때문에
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    # 테이블 초기화
    dp = [0] * (n + 1)
    
    # 초기 값 설정
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1234567
    
    return dp[n]
