def solution(board, h, w):
    count=0
    n=len(board)
    dh=[0,1,-1,0]
    dw=[1,0,0,-1]
    for i in range(0,4):
        h_ch=h+dh[i]
        w_ch=w+dw[i]
        if 0<= h_ch<n and 0<=w_ch<n :
            if board[h_ch][w_ch]==board[h][w]:
                count+=1
    return count