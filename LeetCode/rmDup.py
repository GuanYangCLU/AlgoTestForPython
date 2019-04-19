nums = []

def removeDuplicates(nums):
    l = len(nums)
    cut = 0
    for i in range(len(nums)):
        if i == 0:
            pass
        # elif i >= l:
            # return l        
        else:
            # print(i,nums[i],nums[i-1])
            if nums[i] == nums[i-1]:
                nums.pop(i)
                nums.insert(0,-1) # insert -1 in the start of list to guarantee the position of i
                cut += 1
                l -= 1
                # print(l)
    #print(nums[cut:len(nums)])
    for i in range(cut):
        nums.pop(0)
    return l
    
nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
print(nums)