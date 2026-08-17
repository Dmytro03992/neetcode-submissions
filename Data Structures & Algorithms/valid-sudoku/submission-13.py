class Solution:
    def columnDuplicates(self, column: List[str]) -> bool: 
        freq = {}

        for i in column:
            if i.isdigit():
                freq[i] = freq.get(i, 0) + 1
        for i in freq.values():
            if i > 1:
                return True
        return False

    def rowToColumn(self, row: List[List[str]], index: int) -> List[str]:
        column = []
        for i in range(len(row)):
            column.append(row[i][index])

        return column

    def Block(self, board: List[List[str]], indexY: int, indexX: int) -> List[str]:
        indexY = indexY // 3 * 3
        indexX = indexX // 3 * 3
        row = []
        for i in range(indexY, indexY+3):
            for j in range(indexX, indexX + 3):
                row.append(board[i][j])
        
        return row

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.columnDuplicates(board[i]) or self.columnDuplicates(self.rowToColumn(board, i)) or self.columnDuplicates(self.Block(board, i, j)):
                    return False

        return True