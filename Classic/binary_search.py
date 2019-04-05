def BS(n,arr):
    return helper(n,arr,0,len(arr)-1)
def helper(n,arr,left,right):
    if left == right:
        return -1
    med = left + (left+right)//2
    if arr(med) < n:
        return helper(n,arr,med+1,right)
    elif: arr(med) > n:
        return helper(n,arr,left,med)
    else: return med
    
