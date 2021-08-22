class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return self.getGCD(min(nums), max(nums))
    def getGCD(self, a, b):
        if a > b:
            a, b = b, a
        while b % a > 0:
            b %= a
            if a > b:
                a, b = b, a
        return a
        
