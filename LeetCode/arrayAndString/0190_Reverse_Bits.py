class Solution:
    """
    @param n: an integer
    @return: return an integer
    """
    def reverseBits(self, n):
        # write your code here
        binStr = str(bin(n))[2:]
        fullStr = '0' * (32 - len(binStr)) + binStr
        return int(fullStr[::-1], 2)
        
