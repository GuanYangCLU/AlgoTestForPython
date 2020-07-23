    def kthLargestElement(self, n, nums):
        # write your code here
        lst = nums[:]
        while n <= len(lst):
            if > len(lst) // 2 + 1:
                
            
        
    def getHalf(self, lst):
        if len(lst) == 1:
            return lst
        if len(lst) % 2 == 1:
            halfMax = lst[-1]
            for i in range(len(lst) - 1):
                if lst[i] > lst[i + (len(lst) - 1) // 2]:
                    lst[i], lst[i + (len(lst) - 1) // 2] = lst[i + (len(lst) - 1) // 2], lst[i]
                    halfMax = max(halfMax, lst[i])
            return [halfMax] + lst[[i + (len(lst) - 1) // 2:]
        for i in range(len(lst)):
            lst[i], lst[i + len(lst) // 2] = lst[i + len(lst) // 2], lst[i]
            return lst[i + len(lst) // 2:]
