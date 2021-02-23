class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        monotone_stack = []
        for n in nums2:
            while monotone_stack and monotone_stack[-1] < n:
                # n start insert in to stack and kick top eles out
                res[monotone_stack.pop()] = n
            # if n less than top, pushed in
            monotone_stack.append(n)
        for el in monotone_stack:
            # these ele no more ele greater after them
            res[el] = -1
        return [res[item] for item in nums1]
    
