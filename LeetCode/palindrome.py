class Solution:
    def isPalindrome(self, x):
        lst = list(str(x))
        lst2 = lst[::-1]
        if lst == lst2:
            return True
        else:
            return False
p = Solution()
print(p.isPalindrome(12321))
'''
if x <= 0:
            return []        
        lst = [x%10]
        #print(a)
        x = x // 10
        #print(x)
        lst.extend(self.isPalindrome(x)) 
'''
# def test(lst):
    #lst = [1,2,3,3,2]
    # lst2 = lst.reverse()    lst.reverse()只能作用于自身，这里lst2未能被赋值，仍为None，lst被改变
    # print(lst,lst2)
# test([1,2,3,3,2])