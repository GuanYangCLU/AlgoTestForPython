class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if not moves:
            return true
        arrU = 0
        arrD = 0
        arrL = 0
        arrR = 0
        for i in range(len(moves)):
            if moves[i] == 'U':
                arrU += 1
            if moves[i] == 'D':
                arrD += 1
            if moves[i] == 'L':
                arrL += 1
            if moves[i] == 'R':
                arrR += 1
        return arrU == arrD and arrL == arrR
