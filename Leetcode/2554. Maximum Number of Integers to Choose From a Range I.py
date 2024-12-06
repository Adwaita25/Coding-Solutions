class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set = set(banned)
        total, count = 0, 0

        for i in range(1, n+1):
            if i in banned_set:
                continue
            total += i
            if total > maxSum:
                break
            count += 1
        return count
