class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                # bad case, seperate them let them won't back to before case
                right -= 1
                left += 1
            elif nums[left] <= nums[mid]:
                # in ascending scale
                if target >= nums[left] and target < nums[mid]:
                    # normal inside
                    right = mid - 1
                else:
                    # in right half
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
        
