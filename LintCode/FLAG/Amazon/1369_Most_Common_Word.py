# Lint Amazon Ladder 1
# https://www.jiuzhang.com/problem/most-common-word/
import re

class Solution:
    """
    @param paragraph: 
    @param banned: 
    @return: nothing
    """
    def mostCommonWord(self, paragraph, banned):
        # refer the one line return
        wordList = re.findall(r'\w+', paragraph.lower())
        banSet = set(banned)
        # return collections.Counter(w for w in wordList if w not in banSet).most_common(1)[0][0]
        wordDict = {}
        mostWord, freq = '', 0
        for word in wordList:
            if word in banSet:
                continue
            curWordFreq = wordDict.get(word, 0) + 1
            wordDict[word] = curWordFreq
            if curWordFreq > freq:
                mostWord, freq = word, curWordFreq
        return mostWord
