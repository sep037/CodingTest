def solution(s):
    num = list(map(int, s.split()))
    
    max_value = max(num)
    min_value = min(num)
    
    return f"{min_value} {max_value}"