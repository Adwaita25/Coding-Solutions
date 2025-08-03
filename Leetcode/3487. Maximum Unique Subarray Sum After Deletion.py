class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if all(n<0 for n in nums):
            return max(nums)
        
        set_nums = set(nums)
        return sum(n for n in set_nums if n>0)
