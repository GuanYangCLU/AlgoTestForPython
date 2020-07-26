class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return []
        if len(arr) < 2 and k < 2:
            return arr
        left, right = 0, len(arr) - k
        while left + 1 < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid
                continue
            right = mid
        
        start = right if x - arr[left] > arr[left + k] - x else left
        
        return arr[start:start + k]
