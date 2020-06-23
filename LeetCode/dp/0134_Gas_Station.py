class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        left = [fill - loss for (fill, loss) in zip(gas, cost)]
        print(left)
        l = len(left)
        dp = [True] * l
        for i in range(l):
            balance = 0
            for j in range(i, i + l):
                balance += left[j % l]
                dp[i] = dp[i] and balance >= 0
                if not dp[i]:
                    break
        if True in dp:
            return dp.index(True)
        return -1
    '''
    better way to reuse results of diff(gas, cost)
    tank = gap = start = 0
    for i in range(len(gas)):
        tank += gas[i]
        if tank >= cost[i]:
            tank -= cost[i]
        else:
            gap += cost[i] - tank
            start = i + 1
            tank = 0
    if start == len(gas) or tank < gap: return -1
    return start
    '''
