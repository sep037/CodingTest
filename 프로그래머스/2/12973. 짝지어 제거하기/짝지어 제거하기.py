def solution(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # 같은 알파벳이 연속된 경우 제거
        else:
            stack.append(char)  # 그렇지 않으면 스택에 추가

    # 스택이 비어 있으면 성공적으로 제거된 것임 ~ . ~
    return 1 if not stack else 0
