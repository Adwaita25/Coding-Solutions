class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
        res = []
        for i,n in enumerate(nums):
            if n>0:
                res.append(i+1)
        return res
