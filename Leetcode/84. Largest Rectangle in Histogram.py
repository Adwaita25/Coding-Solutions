class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, ans = [], 0

        for i, n in enumerate(heights + [0]):
            while stack and heights[stack[-1]] >= n:
                H = heights[stack.pop()]
                if not stack:
                    W = i
                else:
                    W = i - stack[-1] - 1
                ans = max(ans, H*W)
            stack.append(i)
        return ans
