from typing import List

class Solution:
    def issafe(self,row,col,board,n,horizontal,lower_diagonal,upper_diagonal):
        #check_horizontal
        if horizontal[row]==1:
            return False
        elif lower_diagonal[row+col]==1:
            return False
        elif upper_diagonal[(n-1)+(col-row)]==1:
            return False
        return True

    def solve(self,board,n,result,col,horizontal,lower_diagonal,upper_diagonal):
        if col==n:
            result.append(board.copy())
            return
        for row in range(n):
            if self.issafe(row,col,board,n,horizontal,lower_diagonal,upper_diagonal):
                board[row]=board[row][:col]+"Q"+board[row][col+1:]
                #set all trackings to 1
                horizontal[row]=1
                lower_diagonal[row+col]=1
                upper_diagonal[(n-1)+(col-row)]=1

                self.solve(board,n,result,col+1,horizontal,lower_diagonal,upper_diagonal)
                board[row]=board[row][:col]+"."+board[row][col+1:]       
                #set all trackings to 0 back         
                horizontal[row]=0
                lower_diagonal[row+col]=0
                upper_diagonal[(n-1)+(col-row)]=0

    def solveNQueens(self, n: int) -> List[List[str]]:
        diagonal_count =(2*n)-1
        horizontal=[0 for _ in range(n)]
        lower_diagonal=[0 for _ in range(diagonal_count)]
        upper_diagonal=[0 for _ in range(diagonal_count)]
        board=["."*n for _ in range(n)]
        result=[]
        self.solve(board,n,result,0,horizontal,lower_diagonal,upper_diagonal)
        return result


