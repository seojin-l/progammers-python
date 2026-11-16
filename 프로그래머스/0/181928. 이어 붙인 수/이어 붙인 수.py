def solution(num_list):
    answer = 0
    odd=[]
    even=[]
    for i in range(0,len(num_list)):
        if num_list[i]%2==0:
            even.append(num_list[i])
        else:
            odd.append(num_list[i])
    odd_num=""
    even_num=""
    for i in odd:
        odd_num+=str(i)
    for i in even :
        even_num+=str(i)
    return int(odd_num)+int(even_num)