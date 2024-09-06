def solution(brown, yellow):
    total = brown + yellow
    
    for height in range(1, int(total ** 0.5) + 1):
        if total % height == 0: #세로가 나눠 떨어지는지 확인하기
            width = total // height
            
            # 갈색 격자는 테두리를 차지하므로 (width - 2) * (height - 2)가 노란색 격자의 수와 같아야 함
            if (width - 2) * (height - 2) == yellow:
                return [width, height]
