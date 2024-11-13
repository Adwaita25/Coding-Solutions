class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res1 = []
        res2 = []

        for i in nums1:
            if i not in nums2 and i not in res1:
                res1.append(i)
        for j in nums2:
            if j not in nums1 and j not in res2:
                res2.append(j)
        return [res1, res2]
