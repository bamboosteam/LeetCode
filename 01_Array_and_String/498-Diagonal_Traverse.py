"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

"""

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def go_up(mat: List[List[int]], curr: List[int], ans: List[int]):
            row, col = curr[0], curr[1]
            if row == m - 1 and col == n - 1: return
            row -= 1
            col += 1
            # move to go_down with one step below node
            if col >= n:
                row, col = min(row + 2, m - 1), n - 1
                ans.append(mat[row][col])
                return go_down(mat, [row, col], ans)
            # move to go_down with one step right node
            elif row < 0:
                row, col = 0, min(n - 1, col)
                ans.append(mat[row][col])
                return go_down(mat, [row, col], ans)
            else:
                ans.append(mat[row][col])
                return go_up(mat, [row, col], ans)

        def go_down(mat: List[List[int]], curr: List[int], ans: List[int]):
            row, col = curr[0], curr[1]
            if row == m - 1 and col == n - 1: return
            row += 1
            col -= 1
            # move to go_up with one step right node
            if row >= m:
                row, col = m - 1, min(col + 2, n - 1)
                ans.append(mat[row][col])
                return go_up(mat, [row, col], ans) 
            # move to go_up with one step below node
            elif col < 0:
                row, col = min(m - 1, row), 0
                ans.append(mat[row][col])
                return go_up(mat, [row, col], ans)
            else:
                ans.append(mat[row][col])
                return go_down(mat, [row, col], ans)

        row, col = 0, 0
        m, n = len(mat), len(mat[0])
        ans = []
        ans.append(mat[row][col])
        go_up(mat, [row, col], ans)
        
        return ans                