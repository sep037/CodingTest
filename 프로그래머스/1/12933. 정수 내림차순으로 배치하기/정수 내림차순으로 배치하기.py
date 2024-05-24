def solution(n):

    str_n = str(n)

    list_n = list(str_n)
    
    sorted_list_n = sorted(list_n, reverse=True)
    
    sorted_str_n = ''.join(sorted_list_n)
    
    answer = int(sorted_str_n)
    
    return answer
