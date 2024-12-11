class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1
        
        nums = sorted(nums)
        
        left, right = 0, len(nums) - 1
        mid = (left + right)//2
        return nums[mid]
