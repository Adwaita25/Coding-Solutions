class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start == target:
            return True
        waitL, waitR = 0, 0

        for curr, dest in zip(start, target):
            if curr == 'R':
                if waitL > 0:
                    return False
                waitR += 1
            if dest == 'L':
                if waitR > 0:
                    return False
                waitL += 1
            if dest == 'R':
                if waitR == 0:
                    return False
                waitR -= 1
            if curr == 'L':
                if waitL == 0:
                    return False
                waitL -= 1
        return waitL == 0 and waitR == 0
