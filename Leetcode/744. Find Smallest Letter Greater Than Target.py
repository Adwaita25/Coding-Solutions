class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low, high = 0, len(letters) - 1
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        
        while(low <= high):
            mid = (low+high)//2
            if letters[mid] <= target:
                low = mid +1
            else:
                high = mid - 1
        return letters[low]
