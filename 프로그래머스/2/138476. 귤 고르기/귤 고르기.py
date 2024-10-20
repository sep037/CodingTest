from collections import Counter

def solution(k, tangerine):
    # 귤 크기별 개수를 센다.
    count = Counter(tangerine)
    
    # 귤 크기별 개수를 내림차순으로 정렬한다.
    sorted_counts = sorted(count.values(), reverse=True)
    
    # 가장 많은 귤부터 선택하면서 k개를 고른다.
    total = 0
    kinds = 0
    for c in sorted_counts:
        total += c
        kinds += 1
        if total >= k:
            break
    
    # 선택한 귤 크기의 종류를 반환한다.
    return kinds
