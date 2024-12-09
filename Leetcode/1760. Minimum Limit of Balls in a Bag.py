class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
    
        while left < right:
            mid = (left + right) // 2        
            total = 0
            for i in nums:
                contribution = (i - 1) // mid
                total += contribution
            
            if total > maxOperations:
                left = mid + 1
            else:
                right = mid
        
        return left
