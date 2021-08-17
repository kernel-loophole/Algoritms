class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in board:
            check_row=[]
            columns_check=[]
            for j in i:
                if j.isdigit():
                    if j in check_row:
                        return False
                    # print(j)
                    check_row.append(j)

        for col in range(9):  # There are 9 columns in a Sudoku grid
            column_values = [row[col] for row in board]
            for check in range(0,len(column_values)):
                if column_values[check] in column_values and column_values[check]!='.':
                    try: 
                        index_of=column_values.index(column_values[check])
                        # print(index_of)
                        if column_values.index(column_values[check])!=check:
                            print(column_values[check])
                            print("flase ruturn")
                            return False
                    except:
                        pass
        subgrids = []

        # Iterate through each 3x3 subgrid
        for i in range(0, 9, 3):  # Rows
            for j in range(0, 9, 3):  # Columns
                subgrid = []
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        subgrid.append(board[row][col])
                for check in range(0,len(subgrid)):
                    if subgrid[check] in subgrid and subgrid[check]!='.':
                        try: 
                            index_of=subgrid.index(subgrid[check])
                            # print(index_of)
                            if subgrid.index(subgrid[check])!=check:
                                #print("flase ruturn")
                                return False
                        except:
                            pass
                subgrids.append(subgrid)
        return True

if __name__=="__main__":
    s=Solution()
    board=[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","3"]
,["8",".",".",".","6",".",".",".","."]
,["4",".",".","8",".","3",".",".","5"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","."]
,[".",".",".",".","8",".",".","7","9"]]
    s.isValidSudoku(board)
                    
