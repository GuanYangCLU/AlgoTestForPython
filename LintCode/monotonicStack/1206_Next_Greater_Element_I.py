class Solution:
    """
    @param nums1: an array
    @param nums2: an array
    @return:  find all the next greater numbers for nums1's elements in the corresponding places of nums2
    """
    def nextGreaterElement(self, nums1, nums2):
        # Write your code here
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
        
