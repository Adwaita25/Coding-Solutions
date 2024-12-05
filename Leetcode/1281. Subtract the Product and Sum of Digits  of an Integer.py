class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digit_prod = 1
        digit_sum = 0
        while n:
            temp = n%10
            digit_prod *= temp
            digit_sum += temp
            n = n//10
        return digit_prod - digit_sum
