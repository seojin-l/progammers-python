def solution(food):
    result=''
    ans=''
    for i in range(1,len(food)) :
        r=0
        d=0
        if food[i] >= 2 :
            r=food[i]//2
            d=food[i]%2
            result+=str(i)*r
    ans=result+str(0)+result[::-1]
    return ans