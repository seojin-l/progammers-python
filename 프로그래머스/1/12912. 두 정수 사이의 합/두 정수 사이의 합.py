def solution(a, b):
    if a > b :
        t=a
        a=b
        b=t
    
    answer=a
    if a==b :
        return a
    else :
        while a < b :
            answer+=a+1
            a+=1
            
    return answer
        
 