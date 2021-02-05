class Solution:
    """
    @param s: A string
    @param dict: A set of word
    @return: the number of possible sentences.
    """
    def wordBreak3(self, s, dict):
        # Write your code here
        sentence = s.lower()
        wordSet = set([word.lower() for word in dict])
        # dp[i] means sentence of first length i, number of answers
        dp = [0] * (len(sentence) + 1)
        dp[0] = 1 # when is ''
        for i in range(0, len(sentence)):
            for j in range(i + 1, len(sentence) + 1):
                if sentence[i:j] in wordSet:
                    # merge dp[i] only once, because i never move back, but will merge different values of i
                    dp[j] += dp[i]
        return dp[-1]
        
# to do: dfs memorization:
