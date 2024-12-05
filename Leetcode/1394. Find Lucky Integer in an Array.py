class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        count = {}
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        for i in count:
            if count[i] == i:
                res = max(res, i)
        return res
