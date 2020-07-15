class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst = sorted(nums)
        res = []
        for n in nums:
            res.append(lst.index(n))
        return res
