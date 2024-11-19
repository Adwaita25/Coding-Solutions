class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        elements = set()
        curr_sum, max_sum = 0, 0
        left = 0

        for right in range(n):
            if nums[right] not in elements:
                curr_sum += nums[right]
                elements.add(nums[right])

                if right - left + 1 == k:
                    if curr_sum > max_sum:
                        max_sum = curr_sum
                    curr_sum -= nums[left]
                    elements.remove(nums[left])
                    left += 1
            else:
                while nums[left] != nums[right]:
                    curr_sum -= nums[left]
                    elements.remove(nums[left])
                    left += 1
                left += 1
        return max_sum
