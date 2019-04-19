class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]
    # def get_bin(self, n):
    #     lst = []
    #     ans = ''
    #     while n != 0:
    #         lst.append(n%2)
    #         n = n//2
    #     while not lst:
    #         ans += str(lst.pop())
    #     return ans