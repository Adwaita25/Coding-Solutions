class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in prev:
                return [prev[difference], i]
            prev[n] = i
        return
