class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = {(0, 0): float(poured)}

        def pour(row):
            if row == query_row:
                return min(1.0, dp.get((row, query_glass), 0.0))

            for col in range(row + 1):
                water = dp.get((row, col), 0.0)

                if water > 1:
                    overflow = water - 1
                    dp[(row, col)] = 1.0

                    dp[(row + 1, col)] = dp.get((row + 1, col), 0.0) + overflow / 2
                    dp[(row + 1, col + 1)] = dp.get((row + 1, col + 1), 0.0) + overflow / 2

            return pour(row + 1)

        return pour(0)