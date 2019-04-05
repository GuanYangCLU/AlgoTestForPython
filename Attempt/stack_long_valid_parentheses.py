def LVP(str):
    lst = list(str)
    tmp_lst = []
    l = 0
    l_lft = 0
    maxlen = 0
    maxlenz = 0 # 尾部临时最大值
    peak = 0 # 最大左括号堆叠
    for i in range(len(lst)):
        # if i == len(lst)-1  and i > 0 and l_lft > 0:
            # maxlen = 2*(peak - l_lft) if 2*(peak - l_lft) > (l - 2*peak + l_lft + 1) else (l - 2*peak + l_lft + 1)        
        if lst[i] == '(':
            # tmp_lst.pop()
            tmp_lst.append(lst[i])
            l_lft +=1
            peak += 1
            # print(tmp_lst)
            if i == len(lst)-1  and i > 0 and l_lft > 0:
                maxlenz = 2*(peak - l_lft) if 2*(peak - l_lft) > (l - 2*peak + l_lft + 1) else (l - 2*peak + l_lft + 1)
                maxlen = maxlenz if maxlenz > maxlen else maxlen
                l = 0
        elif lst[i] == ')' and l_lft > 0:
            tmp_lst.pop()
            if not tmp_lst:
                peak = 0
            l_lft -= 1
            l += 2
            # print(tmp_lst)
            if i == len(lst)-1  and i > 0:
                maxlenz = 2*(peak - l_lft) if 2*(peak - l_lft) > (l - 2*peak + l_lft) else (l - 2*peak + l_lft)
                maxlen = maxlenz if maxlenz > maxlen else maxlen
                l = 0
        elif lst[i] == ')' and l_lft == 0:
            maxlen = l if maxlen < l else maxlen
            # print(l)
            tmp_lst = []
            l = 0
            peak = 0

        else:
            pass
            # print(tmp_lst)
        maxlen = l if maxlen < l else maxlen
        print(i,l_lft,maxlen,peak)
    
    return maxlen
    
str = '(()(())' #6
str2 = '())()()' #4
str3 = ')()())' #4
str4 = '(()' #2
str5 = '()(()' #2 此情况右边可能连续也可能还未完结连续
str6 = ')()())()()(' #4
str7 = '(()))())(' #4
str8 = '(()(((()' #2 最终陷入的泥潭，无法解keep pushing时的是否关联
print(LVP(str))
print(LVP(str2))
print(LVP(str3))
print(LVP(str4))
print(LVP(str5))
print(LVP(str6))
print(LVP(str7))
print(LVP(str8))