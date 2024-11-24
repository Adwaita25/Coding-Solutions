class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left, right = 1, m*n
        while left < right:
            mid, count = (left+right)//2, 0
            for i in range(1, m+1):
                if n < mid//i:
                    count += n
                else:
                    count += mid//i
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return left
