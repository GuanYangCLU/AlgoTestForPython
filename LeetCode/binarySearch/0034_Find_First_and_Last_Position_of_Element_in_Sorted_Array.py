class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        def searchMin(target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        start = searchMin(target)
        end = searchMin(target+1) - 1
        if not target in nums[start:start+1]:
            return [-1, -1]
        return [start, end]
        # left, right = 0, len(nums) - 1
        # mid = (left + right) // 2
        # lm = mr = -1
        # flag = True
        # while left <= mid <= right and flag:
        #     if nums[mid] == target:
        #         lm, mr = mid, mid
        #         while left < lm <= mid:
        #             if nums[lm] == nums[mid]:
        #                 print(lm)
        #                 lm = (left + lm) // 2
        #             elif nums[lm] < nums[mid]:
        #                 print(lm)
        #                 lm = (lm + mid) // 2 + 1
        #         while mid <= mr < right:
        #             if nums[lm] == nums[mid]:
        #                 mr = (mr + right) // 2 + 1
        #             elif nums[mr] > nums[mid]:
        #                 right = mr
        #                 mr = (mr + mid) // 2
        #         if nums[lm] != nums[mid]:
        #             print(lm)
        #             lm += 1
        #         if nums[mr] != nums[mid]:
        #             mr -= 1
        #         print(lm, mr)
        #         flag = False
        #     elif nums[mid] < target:
        #         left = mid - 1
        #         mid = (left + right) // 2 + 1
        #     elif nums[mid] > target:
        #         right = mid + 1
        #         mid = (left + right) // 2 - 1
        # return [lm, mr]
