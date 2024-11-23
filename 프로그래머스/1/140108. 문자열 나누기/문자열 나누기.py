def solution(s):
    count = 0
    i = 0
    
    while i < len(s):
        x = s[i]
        x_count = 0
        other_count = 0
        j = i
        
        while j < len(s):
            if s[j] == x:
                x_count += 1
            else:
                other_count += 1
            
            if x_count == other_count:
                break
            j += 1
        
        count += 1
        i = j + 1
    
    return count

