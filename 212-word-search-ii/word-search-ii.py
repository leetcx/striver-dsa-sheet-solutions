class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        m = len(board)
        n = len(board[0])

        temp = []
        ans = []
        set1={}
        words = set(words)

        prefixes = set()

        for word in words:
            for i in range(1, len(word) + 1):
                prefixes.add(word[:i])


        def cal(board, i, j):
            nonlocal set1
            
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            curr = "".join(temp)
            if len(temp)>0 and curr not in prefixes:
                return

            

            if curr in words:
                if curr not in ans:
                    ans.append(curr)

            if len(temp) == 0:

                temp.append(board[i][j])

                original = board[i][j]
                board[i][j] = "#"

                cal(board, i, j)

                board[i][j] = original
                temp.pop()

            else:

                # Down
                if i + 1 < m and board[i + 1][j] != "#":

                    temp.append(board[i + 1][j])

                    original = board[i][j]
                    board[i][j] = "#"

                    cal(board, i + 1, j)

                    board[i][j] = original
                    temp.pop()

                # Up
                if i - 1 >= 0 and board[i - 1][j] != "#":

                    temp.append(board[i - 1][j])

                    original = board[i][j]
                    board[i][j] = "#"

                    cal(board, i - 1, j)

                    board[i][j] = original
                    temp.pop()

                # Left
                if j - 1 >= 0 and board[i][j - 1] != "#":

                    temp.append(board[i][j - 1])

                    original = board[i][j]
                    board[i][j] = "#"

                    cal(board, i, j - 1)

                    board[i][j] = original
                    temp.pop()

                # Right
                if j + 1 < n and board[i][j + 1] != "#":

                    temp.append(board[i][j + 1])

                    original = board[i][j]
                    board[i][j] = "#"

                    cal(board, i, j + 1)

                    board[i][j] = original
                    temp.pop()

        for i in range(m):
            for j in range(n):
                cal(board, i, j)

        return ans