class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        min_val = float('inf')
        total = 0
        neg_count = 0

        for row in matrix:
            for val in row:
                if val < 0:
                    neg_count += 1
                abs_val = abs(val)
                min_val = min(min_val, abs_val)
                total += abs_val
        if neg_count %2 == 0:
            return total
        return total - 2*min_val
