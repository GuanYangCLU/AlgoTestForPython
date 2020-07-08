class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[k-1]
        # def findMax(lst):
        #     if len(lst) == 1:
        #         return lst[0]
        #     else:
        #         mid = len(lst) // 2
        #         return max(findMax(lst[0:mid]), findMax(lst[mid:]))
        # res = []
        # for i in range(k):
        #     maxVal = findMax(nums)
        #     res.append(maxVal)
        #     nums.remove(maxVal)
        # return res[-1]
        
