class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # prefix_sum = []
        if not matrix or not matrix[0]:
            self.prefix = []
            return
        
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]  # Extra row/col for easier computation
        
        # Compute prefix sum matrix
        for i in range(m):
            for j in range(n):
                self.prefix[i+1][j+1] = (matrix[i][j] 
                                         + self.prefix[i][j+1] 
                                         + self.prefix[i+1][j] 
                                         - self.prefix[i][j])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # ans = 0
        # r = row1
        # while r <= row2:
        #     ans += sum(self.matrix[r][col1:col2+1])
        #     r+=1
        # return ans
        if not self.prefix:
            return 0  # Handle empty matrix case

        # Use precomputed prefix sum matrix for O(1) query
        return (self.prefix[row2+1][col2+1] 
                - self.prefix[row1][col2+1] 
                - self.prefix[row2+1][col1] 
                + self.prefix[row1][col1])




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)