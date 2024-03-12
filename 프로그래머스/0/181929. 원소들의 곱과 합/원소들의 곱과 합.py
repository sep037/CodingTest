def solution(num_list):
    answer = 0
    answer1 = 1
    answer2 = 0
    
    for i in range(len(num_list)):
        answer1 *= num_list[i]
        answer2 += num_list[i]
        
    answer3 = answer2 ** 2
    
    if answer1 < answer3 :
        answer = 1
    else:
        answer = 0
    
    return answer
