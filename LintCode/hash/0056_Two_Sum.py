class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        hashSet = set()
        for i in range(len(numbers)):
            cp = target - numbers[i]
            if numbers[i] in hashSet:
                return [numbers.index(cp), i]
            hashSet.add(cp)
        return [-1, -1]
