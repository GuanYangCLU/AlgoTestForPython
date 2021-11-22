# https://leetcode.com/problems/bulls-and-cows/discuss/74616/3-lines-in-Python

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # pythonic multiple
        bulls = sum(map(lambda x, y: x == y, secret, guess))
        # bulls = sum(map(operator.eq, secret, guess))
        # bulls = sum(x == y for x, y in zip(secret, guess))
        
        both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))
        # both = collections.Counter(secret) & collections.Counter(guess)
        
        return '%dA%dB' % (bulls, both - bulls)
