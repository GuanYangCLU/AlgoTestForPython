#Solve the 8 queens in 10 line  Ans: 92  Guan 02/26/2018 Ref:V, baidu
def queen (bd,i,N):    # \n global count
    if i==N: print(bd); return #count += 1;
    for j in range(N):
        if not ((i-j) in lst1 or (i+j) in lst2 or j in lst3):
            lst1.append(i-j); lst2.append(i+j); lst3.append(j); bd[i] = j;#i store col value as j to locate pos
            queen(bd,i+1,N)
            lst1.pop();lst2.pop();lst3.pop();
bd = [0 for i in range(8)]
lst1 = [];lst2 = [];lst3 = []; #count = 0 ;          
queen(bd,0,8) #print(count)