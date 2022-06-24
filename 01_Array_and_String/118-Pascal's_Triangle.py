class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            col = [1] * (i + 1)
            for j in range(int(i/2)):
                prev = ans[-1]
                col[j+1], col[-1-j-1] = prev[j] + prev[j+1], prev[-1-j] + prev[-1-j-1]
            ans.append(col)
        return ans