class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        count = 0
        tmp = []
        new = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                count += 1
                tmp.append(nums[i][j])
        if count != r * c: return nums
        else:
            for i in range(r):               
                row = []
                for j in range(c):
                    row.append(tmp[i*c + j])
                new.append(row)
        return new
