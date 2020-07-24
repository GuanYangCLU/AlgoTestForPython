class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        size = 1
        cur = reader.get(size - 1)
        if cur == target:
            return 0
        if cur > target:
            return -1
        
        while reader.get(size - 1) < target:
            size *= 2
            
        left, right = size // 2 - 1, size - 1

        while left + 1 < right:
            leftVal = reader.get(left)
            rightVal = reader.get(right)
            if leftVal == target:
                return left
            if rightVal < target or leftVal > target:
                return -1
            mid = (left + right) // 2
            midVal = reader.get(mid)
            if midVal >= target:
                right = mid
                continue
            if midVal < target:
                left = mid
                
        return right if reader.get(right) == target else -1
