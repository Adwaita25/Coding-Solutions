class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum == target:
                return [l+1, r+1]
                break
            elif currSum > target:
                r -= 1
            else:
                l += 1
        
