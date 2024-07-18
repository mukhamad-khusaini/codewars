def is_solved(board):
    all=board[0]+board[1]+board[2]
    def won(num, arr):
        if (
            (arr[0][0]==num and arr[0][1]==num and arr[0][2]==num) or
            (arr[1][0]==num and arr[1][1]==num and arr[1][2]==num) or
            (arr[2][0]==num and arr[2][1]==num and arr[2][2]==num)
            or
            (arr[0][0]==num and arr[1][0]==num and arr[2][0]==num) or
            (arr[0][1]==num and arr[1][1]==num and arr[2][1]==num) or
            (arr[0][2]==num and arr[1][2]==num and arr[2][2]==num)
            or
            (arr[0][0]==num and arr[1][1]==num and arr[2][2]==num) or
            (arr[0][2]==num and arr[1][1]==num and arr[2][0]==num)
            ):
            return True
        else:
            return False
    
    if(won(1,board)): return 1
    elif(won(2,board)): return 2
    elif(0 in all): return -1
    else: return 0

print(is_solved(
    [[2, 2, 1],
     [1, 1, 2],
     [2, 2, 1]]
    ))

# arr=[[2, 2, 0],
#      [0, 1, 2],
#      [2, 2, 1]]

# print(arr[0] + arr[1] + arr[2])
