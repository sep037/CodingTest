def solution(my_strings, parts):
    answer = ''
    for i in range(len(parts)):
        s,e = parts[i]
        mystring = my_strings[i]
        answer += mystring[s:e+1]
            
    return answer