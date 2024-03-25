def solution(my_string):
    num_alpha = 52
    answer = [0 for b in range(num_alpha)] 
    alpha = []
    
    # 아스키코드 대문자 65~90, 소문자 97~122
    # 알파벳 개수 26개
    
    for i in range(num_alpha):
        if i<26:
            alpha.append(chr(65+i))
            i += 1
        else:
            alpha.append(chr(97+i-26)) # 소문자에 도달할 때는 i가 26이상임. 그래서 i에다가 26을 빼주어야 인덱스 오류가 안 남 !
            i += 1
            
    for k in range(len(my_string)):
        for a in range(len(alpha)):
            if my_string[k] == alpha[a]:
                answer[a] += 1
                
    return answer