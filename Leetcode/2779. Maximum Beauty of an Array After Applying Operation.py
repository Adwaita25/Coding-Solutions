class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        length = 0
        for i in range(len(nums)):
            if nums[i] - nums[length] > k*2:
                length += 1
        return i - length + 1
