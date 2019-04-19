print('sol_1:')
def ctn_arr_max(lst):
    sum = [0 for i in range(len(lst))]
    max_lst = [0 for i in range(len(lst))]
    for i in range(len(lst)):
        if i == 0:
            sum[i] = lst[i]
        else:
            if sum[i-1] > 0:
                sum[i] += (lst[i] + sum[i-1])
            else: sum[i] += lst[i]
            max_lst[i] = max(sum[i-1],sum[i])
            # print(max_lst)
    return max(max_lst)
lst = [1,-4,5,6,-8,-10,10,11,-3, 14]
lst2 = [1,2,-1,3,4,10,10,-10,-1]
print(ctn_arr_max(lst))
print(ctn_arr_max(lst2))


print('sol_2:')
def ctn_arr_max_2(lst):
    sum = [0 for i in range(len(lst))]
    max_lst = 0
    for i in range(len(lst)):        
        sum[i] += lst[i]
        if sum[i-1] > 0:
            sum[i] += sum[i-1]
            max_lst = max(max_lst,max(sum[i-1],sum[i]))
    return max_lst
    
print(ctn_arr_max_2(lst))
print(ctn_arr_max_2(lst2))


# print('sol_3')
# def ctn_arr_max_3(lst):
    # sum = [0 for i in range(len(lst))]
    # for i in range(len(lst)):        
        # sum[i] += lst[i]
        # if sum[i-1] > 0:
            # sum[i] += sum[i-1]
            # max_lst = max(0,max_lst,max(sum[i-1],sum[i]))
    # return max_lst
    
# print(ctn_arr_max_3(lst))
# print(ctn_arr_max_3(lst2))


# print('sol_4')
# def ctn_arr_max_4(lst):
    





# print(ctn_arr_max_4(lst))
# print(ctn_arr_max_4(lst2))