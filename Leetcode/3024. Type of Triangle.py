class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a = nums[0]
        b = nums[1]
        c = nums[2]

        if not (a+b > c and a+c > b and b+c > a):
            return "none"
        elif a == b and b == c:
                return "equilateral"
        elif a != b and b != c and a != c:
            return "scalene"
        else:
            return "isosceles"
