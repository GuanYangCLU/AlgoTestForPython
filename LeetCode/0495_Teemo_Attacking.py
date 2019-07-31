class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        poisonedTime = len(timeSeries) * duration
        for i in range(len(timeSeries) - 1):
            if timeSeries[i] + duration > timeSeries[i+1]:
                poisonedTime -= (timeSeries[i] + duration - timeSeries[i+1])
        return poisonedTime
