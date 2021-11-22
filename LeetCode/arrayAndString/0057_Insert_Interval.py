# https://leetcode.com/problems/insert-interval/discuss/21622/7%2B-lines-3-easy-solutions

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        left, right = newInterval[0], newInterval[1]
        leftItems, rightItems = [], []
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                leftItems += [intervals[i]]
                continue
            if intervals[i][0] > newInterval[1]:
                rightItems += [intervals[i]]
                continue
            left = min(left, intervals[i][0])
            right = max(right, intervals[i][1])

        # print(left, right, leftItems, rightItems)
        overlapItem = [left, right]
        return leftItems + [overlapItem] + rightItems
