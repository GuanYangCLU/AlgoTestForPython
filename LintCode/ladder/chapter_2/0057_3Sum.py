class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        if not numbers or len(numbers) < 3:
            return []
        
        numbers.sort()
        res = []
        for i in range(len(numbers) - 2):
            if numbers[i] > 0:
                break
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            left, right = i + 1, len(numbers) - 1
            target = -numbers[i]
            while left < right:
                sumVal = numbers[left] + numbers[right]
                if sumVal == target:
                    if [numbers[i], numbers[left], numbers[right]] not in res:
                        res.append([numbers[i], numbers[left], numbers[right]])
                    left += 1
                    right -= 1
                    continue
                if sumVal > target:
                    right -= 1
                    continue
                if sumVal < target:
                    left += 1
        return res
