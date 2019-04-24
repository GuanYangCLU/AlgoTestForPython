def longestCommonPrefix(strs):
    # rs = ''
    if not strs: return ''
    if strs[0] == '': return ''
    maxl = len(strs[0])
    for i in range(1, len(strs)):
        cur_max = 0
        if not strs[i]:
            return ''
        for j in range(len(strs[i])):
            if j > len(strs[i-1]) - 1 or strs[i][j] != strs[i-1][j]:
                break
            if strs[i][j] == strs[i-1][j]:
                # print('i do',i,cur_max)
                cur_max += 1
                # print(cur_max, strs[i])
        # print('h',cur_max,maxl,i)
        if cur_max < maxl: maxl = cur_max
        # print(maxl, i)
    return strs[0][0:maxl]

strs = ['flowers','flow','flight']
if __name__ == '__main__' :
    print(longestCommonPrefix(strs))


'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # rs = ''
        if not strs: return ''
        if strs[0] == '': return ''
        maxl = len(strs[0])
        for i in range(1, len(strs)):
            cur_max = 0
            if not strs[i]:
                return ''
            for j in range(len(strs[i])):
                if j > len(strs[i-1]) - 1 or strs[i][j] != strs[i-1][j]:
                    break
                if strs[i][j] == strs[i-1][j]:
                    # print('i do',i,cur_max)
                    cur_max += 1
                    # print(cur_max, strs[i])
            # print('h',cur_max,maxl,i)
            if cur_max < maxl: maxl = cur_max
            # print(maxl, i)
        return strs[0][0:maxl]
'''