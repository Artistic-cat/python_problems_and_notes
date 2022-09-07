"""
Backtracking
Difficulty: Hard

Question:
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]

Constraints:
1 <= n <= 9

Logic:
no same rows
no same columns
no same positive diagonal (r+c equal)
no same negative diagonal (r-c equal)
"""

#Fix this, something in similar lines~

def backtracking(r):
    for c in range(r):

        if c in col or (r+c) in posDiag or (r-c) in negDiag:
            continue
        col.add(c)
        posDiag.add(r+c)
        negDiag.add(r-c)
        board[r][c]="Q"

        queensDontAttack(r+1)

        col.remove(c)
        posDiag.remove(r+c)
        negDiag.remove(r-c)
        board[r][c]="."

def queensDontAttack(r):
    col=()
    posDiag=()
    negDiag=()
    result=[]
    board=["."*n for i in range(r)]

    




n=4
# board=["."*n for i in range(n)]
print(queensDontAttack(n))