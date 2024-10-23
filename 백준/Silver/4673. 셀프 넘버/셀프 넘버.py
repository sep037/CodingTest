def d(n):
    return n + sum(int(digit) for digit in str(n))

# 셀프 넘버를 찾는 함수
def find_self_numbers(limit):
    generated_numbers = set()  # 생성된 숫자를 저장할 집합
    for i in range(1, limit + 1):
        generated_number = d(i)
        if generated_number <= limit:
            generated_numbers.add(generated_number)
    
    # 셀프 넘버는 생성된 숫자 집합에 없는 숫자들
    self_numbers = [i for i in range(1, limit + 1) if i not in generated_numbers]
    return self_numbers


limit = 10000
self_numbers = find_self_numbers(limit)

for number in self_numbers:
    print(number)
