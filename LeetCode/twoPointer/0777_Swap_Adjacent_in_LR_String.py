class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        l = 0
        r = 0
        for i in range(len(start)):
            if start[i] == 'R':
                r += 1
            if start[i] == 'L':
                l += 1
            if end[i] == 'R':
                r -= 1
            if end[i] == 'L':
                l -= 1
            if l > 0 or r < 0 or (l * r < 0):
                return False
        newStart = re.sub('X', '', start)
        newEnd = re.sub('X', '', end)
        l = 0
        r = 0
        if len(newStart) != len(newEnd):
            return False
        for i in range(len(newStart)):
            if newStart[i] == 'R':
                r += 1
            if newStart[i] == 'L':
                l += 1
            if newEnd[i] == 'R':
                r -= 1
            if newEnd[i] == 'L':
                l -= 1
            if l > 0 or r < 0 or (l * r < 0):
                return False
        return l == 0 and r == 0
