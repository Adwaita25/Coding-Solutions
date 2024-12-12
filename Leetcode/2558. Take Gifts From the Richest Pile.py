class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import math
        
        i = 0
        while i < k:
            gifts = sorted(gifts)
            temp = floor(sqrt(gifts[-1]))
            gifts[-1] = temp
            i += 1
        return sum(gifts)
