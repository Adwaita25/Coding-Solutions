class Solution:
    def maximumLength(self, s: str) -> int:
        from collections import Counter
        subarr = []

        for i in range(len(s)):
            index = i
            while index < len(s) and s[index] == s[i]:
                subarr.append(s[i:index+1])
                index += 1
        counter = Counter(subarr)
        maxLen = 0

        for j,n in counter.items():
            if n >= 3:
                if len(j) > maxLen:
                    maxLen = len(j)
        if maxLen == 0:
            return -1
        return maxLen
