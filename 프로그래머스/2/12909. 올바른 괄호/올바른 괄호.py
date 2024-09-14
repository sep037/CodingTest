def solution(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append('(')
        else:
            # 스택이 비어 있는데 ')'가 나오는 경우는 잘못된 경우
            if not stack:
                return False
            stack.pop()
    
    # 모든 괄호가 짝이 맞으면 스택이 비어있어야 함 아 스택 어려워 ,,. ,, .,, ,, ,, ,
    return len(stack) == 0
