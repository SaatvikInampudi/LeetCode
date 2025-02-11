class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #3 checks
        #row
        # rcount = Counter(board[row])
        # visited = []
        for r in range(9):
            visited = []
            for i in board[r]:
                # print(i)
                if i != '.':
                    if i not in visited:
                        visited.append(i)
                    else:
                        return False
        # visited = []
        for c in range(9):
            visited = []
            for r in range(9):
                if board[r][c] != '.':
                    if board[r][c] not in visited:
                        visited.append(board[r][c])
                    else:
                        return False
        
        for r in range(0,9,3):
            for c in range(0,9,3):
                # print(r,c)
                visited = []
                # print('hi')
                for i in range(3):
                    for j in range(3):
                        if board[r+i][c+j] != '.':
                            # if r == 0 and c==6:
                            #     print(visited)
                            #     print(board[r+i][c+j])
                            if board[r+i][c+j] not in visited:
                                visited.append(board[r+i][c+j])
                            else:
                                return False
        
        return True