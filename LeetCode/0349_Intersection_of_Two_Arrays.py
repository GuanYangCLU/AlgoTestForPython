class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1 or not nums2:
            return []
        rs = []
        numLen = min(len(nums1), len(nums2))
        if numLen != len(nums1):
            nums1, nums2 = nums2, nums1
        for i in range(numLen):
            if nums1[i] in nums2 and nums1[i] not in rs:
                rs.append(nums1[i])
        return rs
