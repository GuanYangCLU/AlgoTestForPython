class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        if not A or k == 0:
            return []
            
        left, right = 0, len(A) - 1
        mid = (left + right) // 2
        res = []
        
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid] == target:
                break
            if A[mid] < target:
                left = mid + 1
                continue
            if A[mid] > target:
                right = mid - 1
        
        print(left, right, mid)
        mid = (left + right) // 2
        print(mid)
        closet = min(abs(A[mid - 1] - target) if mid - 1 >= 0 else float('inf'), abs(A[mid] - target), abs(A[mid + 1] - target) if mid + 1 <= len(A) - 1 else float('inf'))
        if mid - 1 >= 0 and abs(A[mid - 1] - target) == closet:
            mid -= 1
        elif abs(A[mid] - target) == closet:
            mid = mid
        elif mid + 1 <= len(A) - 1 and abs(A[mid + 1] - target) == closet:
            mid += 1

        # if left + 1 >= right:
        #     mid = left if abs(A[left] - target) <= abs(A[right] - target) else right
        print(left, right, mid)
        res.append(A[mid])
        k -= 1
        left, right = mid - 1, mid + 1
        
        while k > 0:
            if left >=0:
                print(left, right, '????')

                while (right <= len(A) - 1 and left >=0 and abs(A[left] - target) <= abs(A[right] - target) or right > len(A) - 1) and k > 0 and left >= 0:
                    res.append(A[left])
                    left -= 1
                    k -= 1
                    continue
            if right < len(A):
                print(left, right, '??')
                print(A[left], A[right], '??')
                while (left >=0 and right <= len(A) - 1 and abs(A[left] - target) > abs(A[right] - target) or left < 0) and k > 0 and right <= len(A) - 1:
                    res.append(A[right])
                    right += 1
                    k -= 1
                    continue
            
            
        return res
