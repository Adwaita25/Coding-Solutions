class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        res1 = res2 = 0

        for i in range(1, n+1):
            if i%m == 0:
                res2 += i
            else:
                res1 += i
        return res1-res2
