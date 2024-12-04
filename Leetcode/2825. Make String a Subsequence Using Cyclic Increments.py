class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        left, right = 0, len(str2)
        for i in str1:
            if left < right and (ord(str2[left]) - ord(i))%26 < 2:
                left += 1
        return left == right
