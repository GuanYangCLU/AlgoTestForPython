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

    # Two Pointer:
class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        if not numbers:
            return [-1, -1]
        sortedNums = sorted([ (number, index)
            for index, number in enumerate(numbers)
        ])
        left, right = 0, len(sortedNums) - 1
        while left < right:
            if sortedNums[left][0] + sortedNums[right][0] == target:
                return sorted([sortedNums[left][1], sortedNums[right][1]])
            if sortedNums[left][0] + sortedNums[right][0] > target:
                right -= 1
                continue
            if sortedNums[left][0] + sortedNums[right][0] < target:
                left += 1
        return [-1, -1]
