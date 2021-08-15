# https://lotabout.me/2018/binary-indexed-tree/
# https://www.jiuzhang.com/problem/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        length = len(nums)
        bitree = [0] * (length + 1)
        res = []
        # to let lowbit match each index, we need let index 0 out of bitree
        # discretize array, if val dup then overwrite index, so will only have largest index among dups
        discreteDict = { val: i + 1 for i, val in enumerate(sorted(nums)) }
        for n in reversed(nums):
            rank = discreteDict[n]
            # if ele is the least, return 0 which is bitree[0] init value
            res.append(self.getSum(bitree, rank - 1))
            self.update(bitree, rank, length)
        return res[::-1]
    
    def getSum(self, bitree, rank):
        count = 0
        idx = rank
        # find all its left parent node data, sum all to get range sum
        # idx == 0: left boundary
        while idx > 0:
            count += bitree[idx]
            idx -= self.getLowBit(idx)
        return count
    
    def update(self, bitree, rank, length):
        idx = rank
        # update self and all right parent node data till out of right boundary
        # do not need to update all index becasue we just use parent data to sum
        while idx <= length:
            bitree[idx] += 1
            idx += self.getLowBit(idx)
            
    def getLowBit(self, i):
        # it is the distance to your direct parent, if no parent you can assume that index
        return i & -i
