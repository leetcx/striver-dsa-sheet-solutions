class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        stringarg = []
        for i in 'abc':
            stringarg.append(i)

        ans = []
        temp = []
        count = 0
        found = False

        def larg(i):
            nonlocal ans
            nonlocal temp
            nonlocal count
            nonlocal found

            if found:
                return

            if len(temp) == n:
                count += 1

                if count == k:
                    ans.append("".join(temp))
                    found = True
                return

            if i >= 3:
                return

            if len(temp) == 0 or temp[-1] != stringarg[i]:
                temp.append(stringarg[i])
                larg(0)
                temp.pop()

            larg(i + 1)

        larg(0)

        if len(ans) == 0:
            return ""

        return ans[0]