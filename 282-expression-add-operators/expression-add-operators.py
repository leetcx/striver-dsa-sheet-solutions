class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:

        def isvalid(temp):
            crazy = []

            i = 0

            # First handle *
            while i < len(temp):

                if temp[i] == "*":
                    a = int(crazy.pop())
                    b = int(temp[i + 1])

                    crazy.append(str(a * b))
                    i += 2

                else:
                    crazy.append(temp[i])
                    i += 1

            # Then handle + and -
            total = int(crazy[0])

            i = 1
            while i < len(crazy):

                if crazy[i] == "+":
                    total += int(crazy[i + 1])

                elif crazy[i] == "-":
                    total -= int(crazy[i + 1])

                i += 2

            return total

        ans = []
        temp = []

        def create(num):

            # No digits left = complete expression
            if len(num) == 0:
                if isvalid(temp) == target:
                    ans.append("".join(temp))
                return

            for i in range(len(num)):

                subnum = num[0:i + 1]
                left = num[i + 1:]

                # Don't allow 05, 00, etc.
                if len(subnum) > 1 and subnum[0] == "0":
                    break

                # Choose the number
                temp.append(subnum)

                # If digits are still left, choose operator
                if len(left) > 0:

                    temp.append("+")
                    create(left)
                    temp.pop()

                    temp.append("-")
                    create(left)
                    temp.pop()

                    temp.append("*")
                    create(left)
                    temp.pop()

                else:
                    # We consumed all digits
                    if isvalid(temp) == target:
                        ans.append("".join(temp))

                # Remove the number
                temp.pop()

        create(num)

        return ans