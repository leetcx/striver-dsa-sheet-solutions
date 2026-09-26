class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
       
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    d = board[i][j]
                    box = (i // 3) * 3 + (j // 3)

                    rows[i].add(d)
                    cols[j].add(d)
                    boxes[box].add(d)
        def solve(board):
            nonlocal rows
            nonlocal cols
            nonlocal boxes
            for i in range(0,9):
                for j in range(0,9):
                    if board[i][j]!=".":
                        continue
                    for d in "123456789":
                        box = (i // 3) * 3 + (j // 3)
                        if d not in rows[i] and d not in cols[j] and d not in boxes[box]:
                            board[i][j]=d
                            rows[i].add(d)
                            cols[j].add(d)
                            boxes[box].add(d)
                            if solve(board):
                                return True
                            board[i][j]="."
                            rows[i].remove(d)
                            cols[j].remove(d)
                            boxes[box].remove(d)
                    return False
            return True
        solve(board)
