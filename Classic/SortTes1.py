lst = ['a', 'b', 'c']
def sorttest (l,r,lst):
    if l == r: print(lst)
    else:
        for i in range(l,r):
            lst[l], lst[i] = lst[i], lst[l]
            sorttest(l+1, r, lst)
            lst[i], lst[l] = lst[l], lst[i]
sorttest(0, len(lst), lst)
