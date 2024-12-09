class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = ans[i-1] + (nums[i] % 2 != nums[i-1] %2)
        res = []
        for i in queries:
            count = ans[i[1]] - ans[i[0]]
            total = i[1] - i[0]
            if total == count:
                res.append(True)
            else:
                res.append(False)
        return res
