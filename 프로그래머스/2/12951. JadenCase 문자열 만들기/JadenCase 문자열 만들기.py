def solution(s):
    answer = ''
    for i in range(len(s)):
        # 첫 문자 또는 이전 문자가 공백인 경우, 대문자로 변환
        if i == 0 or s[i-1] == ' ':
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    return answer
