class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        count = collections.Counter(word2)
        res = 0
        i, j = len(count), 0

        for char in word1:
            count[char] -= 1
            #i -= count[char] == 0
            
            if count[char] == 0:
                i -= 1
            
            while i == 0:
                #i += count[word1[j]] == 0
                if count[word1[j]] == 0:
                    i += 1
                count[word1[j]] += 1
                j += 1
            res += j
        return res
