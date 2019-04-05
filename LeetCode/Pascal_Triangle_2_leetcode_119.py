class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lst = [1]
        for i in range(rowIndex):
            tmp = []
            fake = [0] + lst
            for j in range(len(lst)):                
                tmp.append(fake[j] + fake[j+1])
            lst = tmp + [1]
        return lst