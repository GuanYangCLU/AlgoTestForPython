class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '': return 0
        fast = 0
        slow = 0
        rs = 1
        subl = [s[0]]
        lst = [[0, rs, subl]]
        for i in range(len(s)):
            if s[i] not in lst[i][2]:
                
                pass
                
                # lst.append([i, rs, subl])
            else:
                # rs = max(rs,fast - slow + 1)            
                tmp = subl
                subl = subl[subl.index(s[i])+1::]
                slow += (len(tmp) - len(subl))
                tmp = []
            subl.append(s[i])
            fast += 1
            rs = max(rs,fast - slow + 1)    
            lst.append([i, rs, subl])
        return rs

# ****************精简版**********************
def leng(s):
        if s == '': return 0
        # fast = 0
        slow = 0
        rs = 1
        subl = [s[0]]
        lst = [[0, rs, subl]]  # 保存当前坐标，最大长度，以及当前合法字符串
        for i in range(len(s)):
            if s[i] in lst[i][2]:
                tmp = subl
                subl = subl[subl.index(s[i])+1::]
                slow += (len(tmp) - len(subl))  # 快指针每次恒定移动一格，慢指针在重复时移动n步直到没有重复
                tmp = []
                
            subl.append(s[i])
            # fast += 1
            rs = max(rs,i - slow+2)
            # print(i,fast,slow,rs,subl)
            lst.append([i, rs, subl])
        return rs

# ************************************超精简***********************************
def leng(s):
        if s == '': return 0       
        slow = 0 # fast = 0 # 可用i替代，只是fast比i多走1步，要i-slow+2
        rs = 1
        subl = [s[0]]
        # lst = [[0, rs, subl]]  # 保存当前坐标，最大长度，以及当前合法字符串
        for i in range(len(s)):
            if s[i] in subl:
                slow += (len(subl) - len(subl[subl.index(s[i])+1::]))  # 快指针每次恒定移动一格，慢指针在重复时移动n步直到没有重复 
                subl = subl[subl.index(s[i])+1::]              
            subl.append(s[i])
            # fast += 1
            rs = max(rs,i - slow+2)
            # print(i,slow,rs,subl)
            # lst.append([i, rs, subl])
        return rs
        
s = 'aab'
s2 = 'abcabcbb'
s3 = 'dvdf'
s4 = 'pwwkew'
print(leng(s))
print(leng(s2))
print(leng(s3))
print(leng(s4))        
