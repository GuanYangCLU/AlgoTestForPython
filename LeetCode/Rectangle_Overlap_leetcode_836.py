def isRectangleOverlap(rec1, rec2):
    if ((rec1[0] <= rec2[0] and rec2[0] < rec1[2] or rec2[0] <= rec1[0] and rec1[0] < rec2[2]) and (rec2[1] <= rec1[1] and rec1[1] < rec2[3] or rec1[1] <= rec2[1] and rec2[1] < rec1[3])) or ((rec1[0] < rec2[2] and rec2[2] <= rec1[2] or rec2[0] < rec1[2] and rec1[2] <= rec2[2]) and (rec2[1] < rec1[3] and rec1[3] <= rec2[3] or rec1[1] < rec2[3] and rec2[3] <= rec1[3])):
        return True
    else:
        return False
rec1 = [229,-132,833,833]
rec2 = [-244,-577,837,804]
print(isRectangleOverlap(rec1, rec2))

'''
我们设立两对条件与逆条件(即两个长方形身份对调一下)：
A1（x11<=x21<x12） -- 逆A1（x21<=x11<x22）
B1（y11<=y21<y12） -- 逆B1（y21<=y11<y22）
A2（x11<x22<=x12） -- 逆A2（x21<x12<=x22）
B2（y11<y22<=y12） -- 逆B2（y11<y22<=y12）
逻辑是
（A1 or 逆A1 and B1 or 逆 B1） or （A2 or 逆A2 and B2 or 逆 B2） 为真
'''

'''
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if ((rec1[0] <= rec2[0] and rec2[0] < rec1[2] or rec2[0] <= rec1[0] and rec1[0] < rec2[2]) and (rec2[1] <= rec1[1] and rec1[1] < rec2[3] or rec1[1] <= rec2[1] and rec2[1] < rec1[3])) or ((rec1[0] < rec2[2] and rec2[2] <= rec1[2] or rec2[0] < rec1[2] and rec1[2] <= rec2[2]) and (rec2[1] < rec1[3] and rec1[3] <= rec2[3] or rec1[1] < rec2[3] and rec2[3] <= rec1[3])):
            return True
        else:
            return False
p = Solution()
rec1 = [229,-132,833,833]
rec2 = [-244,-577,837,804]
p.isRectangleOverlap(rec1, rec2)
'''