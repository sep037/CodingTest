def mod_exp(a, b, c): # 분할정복으로 풀어야 시간 초과 안됨 !
    if b == 0: # 지수가 0이면요 그냥 1이에요
        return 1
    elif b % 2 == 0: # 지수가 짝수이면 
        half = mod_exp(a, b // 2, c) 
        return (half * half) % c # 절반씩만 곱하고 그 둘을 곱하기
    else:
        return (a * mod_exp(a, b - 1, c)) % c # 지수를 짝수로 만들고 a를 나중에 한 번 더 곱하기

a, b, c = map(int, input().split())
result = mod_exp(a, b, c)
print(result)
