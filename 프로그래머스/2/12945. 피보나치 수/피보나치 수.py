def solution(n):
    answer = 0
    a = 1
    b = 1
    
    for i in range(1,n):
        if n == 1 or n == 2:
            return 1
        else:
            a,b = b, a+b
        answer = a
                
        
    return a%1234567