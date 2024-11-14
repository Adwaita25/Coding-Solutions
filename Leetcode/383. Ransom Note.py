class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        Hmap = {}

        for char in magazine:
            if char not in Hmap:
                Hmap[char] = 1
            else:
                Hmap[char] += 1
        
        for char in ransomNote:
            if char in Hmap and Hmap[char] > 0:
                Hmap[char] -= 1
            else:
                return False
        return True
