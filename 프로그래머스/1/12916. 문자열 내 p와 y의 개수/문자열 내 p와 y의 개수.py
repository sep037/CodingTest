def solution(s):
    p_num = 0
    y_num = 0
    s2 = s.lower()
    for i in range(len(s)):
        if s2[i] == 'p':
            p_num += 1
        elif s2[i] == 'y':
            y_num += 1
        else: continue
    
    if p_num == y_num:
        return True
    else:
        return False