class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        curr, res = 0, 0
        for i in values:
            res = max(res, curr + i)
            curr = max(curr, i) - 1
        return res
