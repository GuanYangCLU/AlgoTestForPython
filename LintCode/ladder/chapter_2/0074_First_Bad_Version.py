#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        return self.binarySearch(1, n)
        
    def binarySearch(self, start, end):
        while start + 1 < end:
            mid = (start + end) // 2
            ml, mr = SVNRepo.isBadVersion(mid - 1), SVNRepo.isBadVersion(mid)
            if not ml and mr:
                return mid
            if ml and mr:
                end = mid - 1
                continue
            if not ml and not mr:
                start = mid + 1
        return start if SVNRepo.isBadVersion(start) else end
