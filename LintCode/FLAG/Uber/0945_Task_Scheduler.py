class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def leastInterval(self, tasks, n):
        # write your code here
        # cut to mtc slices, first mtc - 1 full of n + 1 time tasks, last tail filled with mtc tasks only
        taskCounts = list(collections.Counter(tasks).values())
        mostTaskCount = max(taskCounts)
        howManyMtcInTask = taskCounts.count(mostTaskCount)
        # in case n too small
        return max((mostTaskCount - 1) * (n + 1) + howManyMtcInTask, len(tasks))
        
