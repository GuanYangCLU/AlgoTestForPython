class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        asc_nums1 = sorted(nums1, key=None)
        desc_nums2 = sorted(nums2, reverse=True)
        return sum([a * b for (a, b) in zip(asc_nums1, desc_nums2)])
        
