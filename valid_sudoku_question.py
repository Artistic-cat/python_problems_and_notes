#Valid Sudoku

"""
You are given a 9x9 array arr
Each digit in arr must appear once in horizontal and verticle line abd box
empty=-1
check if the question is correct.
"""

row=[[0 for i in range(9)] for j in range(9)]
col=[[0 for i in range(9)] for j in range(9)]
box=[[0 for i in range(9)] for j in range(9)]
for i in range(9):
    for j in range(9):
        if arr[i][j]!=-1:
            value=arr[i][j]-1
            boxno=3*(i/3) +(j/3)
            if row[i][value]==1 or col[j][value]==1 or box[boxno][value]==1:
                print("0")
                break
            col[i][value]=1
            row[i][value]=1
            box[i][value]=1
print("1")
