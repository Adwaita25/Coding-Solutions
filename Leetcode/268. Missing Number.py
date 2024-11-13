class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        arrSum = sum(nums)
        total = (n*(n+1))/2

        return int(total - arrSum)
