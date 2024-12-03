class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = []
        a = s1.split(' ') + s2.split(' ')
        dic = {}

        for i in a:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        for i in dic:
            if dic[i] == 1:
                res.append(i)
        return res
        
