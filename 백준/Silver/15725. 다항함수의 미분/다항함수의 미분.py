import sys
import re

input = sys.stdin.read
polynomial = input().strip()

polynomial = polynomial.replace(" ", "")

# 다항식이 'x'를 포함하지 않으면 1차항이 없으므로 0을 출력
if 'x' not in polynomial:
    print(0)

# 'x'를 기준으로 분리 (계수와 상수를 분리)
else:
    # 정규식을 사용하여 'x' 앞의 계수 부분을 추출
    match = re.match(r'([+-]?\d*)x', polynomial)
    
    if match:
        # 'x' 앞의 부분을 추출 (계수가 없는 경우는 1로 간주)
        coefficient = match.group(1)
        
        # 계수가 비어있으면 '1'로 간주
        if coefficient == '' or coefficient == '+':
            print(1)
        elif coefficient == '-':
            print(-1)
        else:
            # 계수가 명시된 경우 정수로 변환 후 출력
            print(int(coefficient))
    else:
        print(0)
