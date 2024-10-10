# 우선 3의 배수는 모든 수를 다 더했을 때 3의 배수여야함
# 30의 배수는 항상 0으로 마무리 ! 니까 0이 없으면 자격 박탈 ㅋ
# 그리고 30의 배수는 결국 3의 배수니까 3의 배수가 아니면 소용 없음을 이용하겟다

N = input().strip()

def makemultiple30(N):
    digits = list(N)
    
    if '0' not in digits:
        return -1

    digit_sum = sum(map(int, digits))
    if digit_sum % 3 != 0:
        return -1

    digits.sort(reverse=True)
    
    return ''.join(digits)

print(makemultiple30(N))
