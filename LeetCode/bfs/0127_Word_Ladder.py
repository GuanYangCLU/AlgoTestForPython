# 双向BFS, 196ms
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 不转set会超时
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        startQueue = collections.deque([beginWord])
        startVisited = set([beginWord])
        endQueue = collections.deque([endWord])
        endVisited = set([endWord])
        distance = 1
        graph = {}
        
        while startQueue and endQueue:
            distance += 1
            if self.extendQueue(graph, startQueue, startVisited, endVisited, wordList):
                return distance
            distance += 1
            if self.extendQueue(graph, endQueue, endVisited, startVisited, wordList):
                return distance
        return 0
    
    def extendQueue(self, graph, queue, visited, oppositeVisited, wordList):
        # print(graph, queue, visited, oppositeVisited)
        # cannot be while queue
        for _ in range(len(queue)):
            word = queue.popleft()
            for nextWord in self.getNextWordList(word, wordList, graph):
                # print(nextWord, word, graph)
                if nextWord in visited:
                    continue
                if nextWord in oppositeVisited:
                    return True
                visited.add(nextWord)
                queue.append(nextWord)
        return False
    
    def getNextWordList(self, word, wordList, graph):
        if word in graph:
            return graph[word]
        nextWordList = []
        for i in range(len(word)):
            left, right = word[:i], word[i+1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char == word[i]:
                    # exact same word
                    continue
                validNextWord = left + char + right
                if validNextWord in wordList:
                    nextWordList.append(validNextWord)
        graph[word] = nextWordList
        return nextWordList
            

# 单向BFS, 348ms
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = collections.deque([beginWord])
        distance = { beginWord: 0 }
        
        while queue:
            word = queue.popleft()
            if word == endWord:
                return distance[word] + 1
            for nextWord in self.getNextWordList(word, wordList):
                if nextWord in distance:
                    continue
                distance[nextWord] = distance[word] + 1
                queue.append(nextWord)
        return 0
    
    def getNextWordList(self, word, wordList):
        nextWordList = []
        for i in range(len(word)):
            left, right = word[:i], word[i+1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if char == word[i]:
                    # exact same word
                    continue
                validNextWord = left + char + right
                if validNextWord in wordList:
                    nextWordList.append(validNextWord)
        return nextWordList
