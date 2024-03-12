def solution(num_list):
    answer = 0
    even_list = ''
    odd_list= ''
    for i in range(len(num_list)):
        if num_list[i]%2 == 0:
            even_list += str(num_list[i])
        else:
            odd_list += str(num_list[i])
            
    answer = int(even_list)+int(odd_list)
            
    return answer