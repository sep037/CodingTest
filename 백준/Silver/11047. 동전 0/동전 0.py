def min_coin(N, K, coin_values):
    # 동전 종류를 큰 값부터 내림차순
    # 큰 값 먼저 써야지 최소 구할 수 잇따
    coin_values.sort(reverse=True)
    
    coin_count = 0  # 동전 개수
    remaining_amount = K  # 남은 금액

    for coin in coin_values:
        if remaining_amount == 0:
            break
        # 현재 동전으로 사용할 수 있는 최대 개수
        num_coins = remaining_amount // coin
        coin_count += num_coins
        remaining_amount -= num_coins * coin

    return coin_count

# 사용자 입력 받기
N, K = map(int, input().split())
coin_values = [int(input()) for _ in range(N)]

# 결과 출력
result = min_coin(N, K, coin_values)
print(result)
