# Better answer in LC
class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end): return False
        
        A = [(s, idx) for idx, s in enumerate(start) if s == 'L' or s == 'R']
        B = [(e, idx) for idx, e in enumerate(end) if e == 'L' or e == 'R']
        if len(A) != len(B): return False
        
        for (s, i), (e, j) in zip(A, B):
            # LR交错了 永不可能
            if s != e: return False
            # 第一个L的位置在start里比在end里更左 由于L只能左移 end不可能有L可以接受这个位置
            if s == 'L':
                if i < j:
                    return False
            if s == 'R':
                if i > j:
                    return False
            
        return True

# fix 9chapter wrong answer
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
