num = 123456 * 2 + 1
num_list = [1] * num

num_list[0] = num_list[1] = 0  # 0과 1은 소수가 아니므로 0으로 설정

for i in range(2, int(num ** 0.5) + 1):
    if num_list[i]:
        for j in range(i * i, num, i):
            num_list[j] = 0

while True:
    n = int(input())
    
    if n == 0:
        break
    
    prime_count = sum(num_list[n+1:2*n+1])
    print(prime_count)
