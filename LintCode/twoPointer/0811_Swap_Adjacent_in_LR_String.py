# https://www.lintcode.com/problem/811/solution/43254
class Solution:
    """
    @param start: the start
    @param end: the end
    @return: is there exists a sequence of moves to transform one string to the other
    """
    def canTransform(self, start, end):
        # Write your code here
        if len(start) != len(end):
            return False
        lst_s = [(s, i) for (i, s) in enumerate(start) if s != 'X']
        lst_e = [(e, j) for (j, e) in enumerate(end) if e != 'X']
        # start end中 LR的整体数目不等
        if len(lst_s) != len(lst_e):
            return False

        for (s, i), (e, j) in zip(lst_s, lst_e):
            # LR交错了，无法通过移动交换他们的位置
            if s != e:
                return False
            # start中的L比end中的更靠左，无法左移至end的L的位置
            if s == 'L' and i < j:
                return False
            if s == 'R' and i > j:
                return False

        return True
