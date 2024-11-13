class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if (mid == left or nums[mid-1] < nums[mid]) and (mid == right or nums[mid] > nums[mid+1]):  # Found peak
                return mid
            if mid == left or nums[mid-1] < nums[mid]:  # Find peak on the right
                left = mid + 1
            else:  # Find peak on the left
                right = mid - 1
        return -1
