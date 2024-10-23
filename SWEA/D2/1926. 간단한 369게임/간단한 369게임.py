def game(N):
    for i in range(1, N + 1):
        # 문자열로 변환하여 "3", "6", "9"의 개수를 셈
        num_str = str(i)
        clap_count = sum([1 for digit in num_str if digit in '369'])
        
        if clap_count > 0:
            # "3", "6", "9"가 포함된 경우 박수 횟수만큼 "-" 출력
            print('-' * clap_count, end=' ')
        else:
            # "3", "6", "9"가 포함되지 않은 경우 숫자 출력
            print(i, end=' ')

N = int(input())
game(N)
