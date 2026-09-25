class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = sorted(tiles)
        used = [False] * len(tiles)
        temp = []
        count = 0

        def cal(i, tiles):
            nonlocal count
            nonlocal used
            nonlocal temp

            if i >= len(tiles) :
                if len(temp)>0:
                    count += 1
                return

            if i < len(tiles) and not used[i]:
                temp.append(tiles[i])
                used[i] = True

                cal(0, tiles)

                used[i] = False
                temp.pop()

            while i + 1 < len(tiles) and tiles[i] == tiles[i + 1] and not used[i]:
                i += 1

            cal(i + 1, tiles)

        cal(0, tiles)
        return count