def solution(s):
    result=s
    num=[0,1,2,3,4,5,6,7,8,9]
    eng=['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(0,len(eng)):
        if eng[i] in s:
            result=result.replace(eng[i],str(num[i]))
    return int(result)
    