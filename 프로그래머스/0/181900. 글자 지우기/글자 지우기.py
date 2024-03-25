def solution(my_string, indices):
    answer = ''
    
    for index, value in enumerate(my_string):
        if index not in indices :
            answer += value
            
    return answer