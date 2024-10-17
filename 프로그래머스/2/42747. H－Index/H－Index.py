def solution(citations):
    # 인용 횟수를 내림차순으로 정렬
    citations.sort(reverse=True)
    
    # 논문 인용 횟수 기준으로 H-Index 계산
    for i in range(len(citations)):
        # 논문 인용 횟수가 i+1 이상이라면 h-index 후보
        if citations[i] < i + 1:
            return i
    
    # 모든 논문이 h-index 후보일 때는 배열 길이가 H-Index
    return len(citations)
