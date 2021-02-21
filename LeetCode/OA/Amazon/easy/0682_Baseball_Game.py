class Solution:
    def calPoints(self, ops: List[str]) -> int:
        if not ops:
            return 0
        i = 0
        while i < len(ops):
            if str(ops[i]) not in 'CD+':
                ops[i] = int(ops[i])
                i += 1
                continue
            if ops[i] == '+':
                ops[i] = ops[i - 1] + ops[i - 2]
                i += 1
                continue
            if ops[i] == 'D':
                ops[i] = 2 * ops[i - 1]
                i += 1
                continue
            if ops[i] == 'C':
                ops.pop(i)
                ops.pop(i - 1)
                i -= 1
            
        return sum(ops)
            
