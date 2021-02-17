class Solution:
    def reverseParentheses(self, s: str) -> str:
        # find next char in a snake order
        if not s:
            return ''
        start, end = 0, len(s) - 1
        fromEndToStart = []
        # record paired index: a -> b, b -> a
        pairIndex = {}
        openedPairIndex = []
        for i, c in enumerate(s):
            if c == '(':
                # got one to stack
                openedPairIndex.append(i)
            elif c == ')':
                # find paired index
                j = openedPairIndex.pop()
                pairIndex[i] = j
                pairIndex[j] = i
        
        curReadIndex, direction = 0, 1
        # find rules from result to start
        while curReadIndex < len(s):
            if s[curReadIndex] in '()':
                # cur index is a pair, go to paired index read in reversed order
                curReadIndex = pairIndex[curReadIndex]
                direction = -direction
            else:
                fromEndToStart.append(s[curReadIndex])
            curReadIndex += direction
        return ''.join(fromEndToStart)

# failed attempt:

class Solution:
    def reverseParentheses(self, s: str) -> str:
        if not s:
            return ''
        start, end = 0, len(s) - 1
        todo = []
        res = ''
        left, right, item = '', '', ['', '']
        stopLeft, stopRight = False, False
        nextLeft, nextRight = 0, len(s) - 1
        while start <= end:
            if not stopLeft:
                if s[start] != '(':
                    left += s[start]
                    # print(left)
                else:
                    stopLeft = True
                    nextLeft = start + 1
                    item[0] = left
                start += 1
            
            if not stopRight:
                if s[end] != ')':
                    right = s[end] + right
                else:
                    stopRight = True
                    nextRight = end - 1
                    item[1] = right
                end -= 1
            
            if stopLeft and stopRight:
                # print('item', item)
                todo.append((item[0], item[1]))
                left, right, item = '', '', ['', '']
                stopLeft, stopRight = False, False
        # print(nextLeft, nextRight, item)
        if nextLeft > nextRight:
            # () in center
            todo.append(('', ''))
        else:
            # (sth)
            # todo.append((s[nextRight:nextLeft - 1:-1], ''))
            todo.append((s[nextLeft:nextRight + 1], ''))
        # print(todo)
        for i in range(len(todo) - 1, -1, -1):
            toReverse = todo[i][0] + res + todo[i][1]
            # print(toReverse, '?')
            res = toReverse if i == 0 else toReverse[::-1] 
            # print(res, '??')
        return res

# test case:
# "(abcd)"
# "(u(love)i)"
# "(ed(et(oc))el)"
# "a(bcdefghijkl(mno)p)q"
