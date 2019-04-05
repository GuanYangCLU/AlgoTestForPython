# N皇后 LeetCode解法，与简单测试版本，此版本为解的list集合[[解1],[解2],...]，其中解是'...Q..'组成的每行字符串，精简版是[1,3,0,2]，[2,0,3,1]，每个数字代表列放皇后的位置
# leetcode 052在最下，未精简，可简化
class Solution:
    lst1 = []; lst2 = []; lst3 = []; 
    def solveNQueens(self, n: int) -> List[List[str]]:
        solu = []
        bd = [0 for i in range(n)]
        Solution.queen(bd,0,n,solu)
        return solu
    def queen (bd,i,n,solu):
        if i==n: 
            ans = [('.' * n) for i in range(n)]
            for i in range(n):
                ans[i] = ans[i][:bd[i]] + 'Q' + ans[i][bd[i]+1:]
            solu.append(ans)
        for j in range(n):
            if not ((i-j) in Solution.lst1 or (i+j) in Solution.lst2 or j in Solution.lst3):
                Solution.lst1.append(i-j)
                Solution.lst2.append(i+j)
                Solution.lst3.append(j)
                bd[i] = j
                
                Solution.queen(bd,i+1,n,solu)
                Solution.lst1.pop()
                Solution.lst2.pop()
                Solution.lst3.pop()
				
'''
# leetcode测试版
def queen (bd,i,n):    # \n global count
    if i==n: #print(bd); return #count += 1;
        ans = [('.' * n) for i in range(n)]
        for i in range(n):
            ans[i] = ans[i][:bd[i]] + 'Q' + ans[i][bd[i]+1:]
        # print(ans)
        solu.append(ans)
        # print(solu)
    for j in range(n):
        if not ((i-j) in lst1 or (i+j) in lst2 or j in lst3):
            lst1.append(i-j); lst2.append(i+j); lst3.append(j); bd[i] = j;#i store col value as j to locate pos
            queen(bd,i+1,n)
            lst1.pop();lst2.pop();lst3.pop();
bd = [0 for i in range(5)]
lst1 = [];lst2 = [];lst3 = []; #count = 0 ; 
solu = []
queen(bd,0,5)
print(solu)
'''


'''
# 精简原始基础版（10行）
def queen (bd,i,N):    # \n global count
    if i==N: print(bd); return #count += 1;
    for j in range(N):
        if not ((i-j) in lst1 or (i+j) in lst2 or j in lst3):
            lst1.append(i-j); lst2.append(i+j); lst3.append(j); bd[i] = j;#i store col value as j to locate pos
            queen(bd,i+1,N)
            lst1.pop();lst2.pop();lst3.pop();
bd = [0 for i in range(4)]
lst1 = [];lst2 = [];lst3 = []; #count = 0 ;          
queen(bd,0,4) #print(count)
'''



'''
# leetcode 052 未精简
class Solution:
    lst1 = []; lst2 = []; lst3 = [];
    def totalNQueens(self, n: int) -> int:
        solu = []
        bd = [0 for i in range(n)]
        Solution.queen(bd,0,n,solu)
        return len(solu)
    def queen (bd,i,n,solu):
        if i==n: 
            ans = [('.' * n) for i in range(n)]
            for i in range(n):
                ans[i] = ans[i][:bd[i]] + 'Q' + ans[i][bd[i]+1:]
            solu.append(ans)
        for j in range(n):
            if not ((i-j) in Solution.lst1 or (i+j) in Solution.lst2 or j in Solution.lst3):
                Solution.lst1.append(i-j)
                Solution.lst2.append(i+j)
                Solution.lst3.append(j)
                bd[i] = j
                
                Solution.queen(bd,i+1,n,solu)
                Solution.lst1.pop()
                Solution.lst2.pop()
                Solution.lst3.pop()
        
'''
