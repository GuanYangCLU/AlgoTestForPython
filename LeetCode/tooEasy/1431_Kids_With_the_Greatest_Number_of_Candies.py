class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxNum = max(candies)
        return [maxNum - candy <= extraCandies for candy in candies]
        
