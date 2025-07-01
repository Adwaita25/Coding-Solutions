class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        minimum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > minimum:
                ans = max(ans, nums[i] - minimum)
            if nums[i] < minimum:
                minimum = nums[i]
        return ans
