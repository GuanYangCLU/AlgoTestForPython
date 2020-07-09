class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        hLeft = hRight = 0
        res = 0
        while left <= right:
            hLeft, hRight = max(hLeft, height[left]), max(hRight, height[right])
            while left <= right and height[left] <= hLeft <= hRight:
                res += (hLeft - height[left])
                left += 1
            while left <= right and height[right] <= hRight <= hLeft:
                res += (hRight - height[right])
                right -= 1
        return res
        
