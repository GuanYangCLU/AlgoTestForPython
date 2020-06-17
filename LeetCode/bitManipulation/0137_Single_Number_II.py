class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a, b = 0, 0
        for i in range(len(nums)):
            # set^value description
            # A^0 = A: add val to set A if val not in A (0 represent)
            # A^A = 0: remove val from set A if val in set A
            # (A ^ n) & ~B add n to A if and only if it not in B else remove from A
            a = (a ^ nums[i]) & (~b)
            b = (b ^ nums[i]) & (~a)
            # first ele will in a, second in b, third will be blocked if b has n
            # ^ on int can be treated as operating in set
        return a
        
