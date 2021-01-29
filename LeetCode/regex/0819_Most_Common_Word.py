# Lint Amazon Ladder 1, LintCode 1369
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
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
        
