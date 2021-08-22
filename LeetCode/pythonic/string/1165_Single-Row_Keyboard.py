class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        l = len(word)
        new_word = keyboard[0] + word
        res = 0
        for i in range(l):
            res += self.getDistance(keyboard, new_word[i], new_word[i + 1])
        return res
        
    def getDistance(self, keyboard, prev, post):
        return abs(keyboard.index(post) - keyboard.index(prev))
        
