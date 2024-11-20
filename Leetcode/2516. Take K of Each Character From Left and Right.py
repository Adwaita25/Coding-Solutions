class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        N = len(s)
        j = 0
        ans = N
        window = 0
        count = {}

        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1
        
        if count.get('a', 0) < k or count.get('b', 0) < k or count.get('c', 0) < k:
            return -1
        
        for i in range(N):
            count[s[i]] -= 1
            window += 1

            while count[s[i]] < k:
                count[s[j]] += 1
                j += 1
                window -= 1

            ans = min(ans, N- window)
        return ans
                
