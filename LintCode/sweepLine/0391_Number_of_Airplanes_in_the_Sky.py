"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        # write your code here
        if not airplanes:
            return 0
        room = []
        for interval in airplanes:
            room.append((interval.start, 1))
            room.append((interval.end, -1))
        
        res = 0
        cur = 0
        
        for time, num in sorted(room):
            cur += num
            res = max(res, cur)
        return res
        
