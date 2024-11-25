def solution(s, n):
    result = []
    for char in s:
        if char.islower():  # 소문자
            result.append(chr((ord(char) - ord('a') + n) % 26 + ord('a')))
        elif char.isupper():  # 대문자
            result.append(chr((ord(char) - ord('A') + n) % 26 + ord('A')))
        else: 
            result.append(char)
    return ''.join(result)