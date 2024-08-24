def solution(s):
    # sort는 리스트만 정렬, sorted는 문자열도 정렬
    sorted_s = sorted(s, reverse=True)
    # 문자열로 합쳐서 반환
    return ''.join(sorted_s)
