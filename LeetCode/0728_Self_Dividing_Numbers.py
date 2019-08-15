class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        rs = []
        i = left
        while i >= left and i <= right:
            if self.checkSDN(i):
                rs.append(i)
            i += 1
        return rs
    
    def checkSDN(self, i):
        for k in range(len(str(i))):
            if int(str(i)[k]) == 0:
                return False
            if i % int(str(i)[k]) != 0:
                return False
        return True
