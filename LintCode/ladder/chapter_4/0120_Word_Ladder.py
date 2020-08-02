class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        dict.add(end)
        queue = collections.deque([start])
        distance = { start: 1 }
        
        while queue:
            word = queue.popleft()
            if word == end:
                return distance[word]
            for next_word in self.get_next_word(word):
                if next_word not in dict or next_word in distance:
                    continue
                queue.append(next_word)
                distance[next_word] = distance[word] + 1
        return 0
        
    def get_next_word(self, word):
        if not word:
            return []
        next_word = []
        for i in range(len(word)):
            left, right = word[:i], word[i+1:]
            for charCode in range(97, 123):
                if chr(charCode) == word[i]:
                    continue
                next_word.append(left + chr(charCode) + right)
        return next_word
