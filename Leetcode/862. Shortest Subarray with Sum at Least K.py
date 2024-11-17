class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sum_arr = [0] * (n+1)

        for i in range(len(nums)):
            sum_arr[i+1] = sum_arr[i] + nums[i]
        
        q = [0] * (n+1)
        left = right = 0
        min_length = n+1

        for i in range(len(sum_arr)):
            while left < right and sum_arr[i] >= sum_arr[q[left]] + k:
                min_length = min(min_length, i-q[left])
                left += 1
            
            while left < right and sum_arr[i] <= sum_arr[q[right - 1]]:
                right -= 1
            
            q[right] = i
            right += 1
        
        if min_length <= n:
            return min_length
        else:
            return -1
