class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # cut to mtc slices, first mtc - 1 full of n + 1 time tasks, last tail filled with mtc tasks only
        taskCounts = list(collections.Counter(tasks).values())
        mostTaskCount = max(taskCounts)
        howManyMtcInTask = taskCounts.count(mostTaskCount)
        # in case n too small
        return max((mostTaskCount - 1) * (n + 1) + howManyMtcInTask, len(tasks))
        
