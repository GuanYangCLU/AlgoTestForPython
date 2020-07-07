class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = {}
        for n in nums:
            if n in dic:
                dic[n] = False
            else:
                dic[n] = True
        return [x for x in dic.keys() if dic[x] == True]
        # zeroSum, zeroProduct = [], []
        # for i in range(len(nums)):
        #     if nums[i] in zeroSum:
        #         zeroSum.append(-nums[i])
        #     else:
        #         zeroSum.append(nums[i])
        #     if nums[i] in zeroProduct:
        #         if nums[i] == 0:
        #             zeroProduct.remove(0)
        #         else:
        #             zeroProduct.append(1 / nums[i])
        #     else:
        #         zeroProduct.append(nums[i])
        # m = sum(zeroSum)
        # n = 1
        # for x in zeroProduct:
        #     n *= x
        # n = int(n)
        # if n == 0:
        #     return [0, m]
        # else:
        #     a = int((m + math.sqrt(m * m - 4 * n)) / 2)
        #     b = int((m - math.sqrt(m * m - 4 * n)) / 2)
        #     return [b, a]
