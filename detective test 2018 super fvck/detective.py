# meta code fot detect, keep it

lst = [0 for i in range(10)]
# def lst_dev():
    # for i in range(10):
        # for j in range(4):
            # lst[i] = 
def ans(lst):
    # for i in range(10):
        # for j in range(4):
    # ans_lst = [0,1,2,3]
    ct_lst = [lst.count(0),lst.count(1),lst.count(2),lst.count(3)]    
    # Q1 write answer in if and ques in do

    # Q2
    if lst[4] == 2:
        lst[1] = 0
    elif lst[4] == 3:
        lst[1] = 1
    elif lst[4] == 0:
        lst[1] = 2
    elif lst[4] == 1:
        lst[1] = 3
    # print(lst[1])
    # Q3
    if lst[2] not in [lst[1],lst[3],lst[5]]:
        lst[2] = 0
    elif lst[5] not in [lst[1],lst[3],lst[2]]:
        lst[2] = 1
    elif lst[1] not in [lst[5],lst[3],lst[2]]:
        lst[2] = 2
    elif lst[3] not in [lst[1],lst[5],lst[2]]:
        lst[2] = 3
    # print(lst[2])
    # Q4
    if lst[0] == lst[4]:
        lst[3] = 0
    elif lst[1] == lst[6]:
        lst[3] = 1
    elif lst[0] == lst[8]:
        lst[3] = 2
    elif lst[5] == lst[9]:
        lst[3] = 3
    # Q5
    if lst[7] == lst[4]:
        lst[4] = 0
    elif lst[3] == lst[4]:
        lst[4] = 1
    elif lst[4] == lst[8]:
        lst[4] = 2
    elif lst[4] == lst[6]:
        lst[4] = 3
    # Q6
    if (lst[7] == lst[1]) and (lst[7] == lst[3]):
        lst[5] = 0
    elif (lst[7] == lst[0]) and (lst[7] == lst[5]):
        lst[5] = 1
    elif (lst[7] == lst[2]) and(lst[7] == lst[9]):
        lst[5] = 2
    elif (lst[7] == lst[4]) and (lst[7] == lst[8]):
        lst[5] = 3
    # Q7
    if lst.count(2) == min(ct_lst):
        lst[6] = 0
    elif lst.count(1) == min(ct_lst):
        lst[6] = 1
    elif lst.count(0) == min(ct_lst):
        lst[6] = 2
    elif lst.count(3) == min(ct_lst):
        lst[6] = 3
    # Q8
    if (abs(lst[6] - lst[0]) == 2) or (abs(lst[6] - lst[0]) == 3):
        lst[7] = 0
    elif (abs(lst[4] - lst[0]) == 2) or(abs(lst[4] - lst[0]) == 3):
        lst[7] = 1
    elif (abs(lst[1] - lst[0]) == 2) or (abs(lst[1] - lst[0]) == 3):
        lst[7] = 2
    elif (abs(lst[9] - lst[0]) == 2) or (abs(lst[9] - lst[0]) == 3):
        lst[7] = 3
    # Q9
    if not (lst[0] == lst[5]) == (lst[5] == lst[4]):
        lst[8] = 0
    elif not (lst[0] == lst[5]) == (lst[9] == lst[4]):
        lst[8] = 1
    elif not (lst[0] == lst[5]) == (lst[1] == lst[4]):
        lst[8] = 2
    elif not (lst[0] == lst[5]) == (lst[8] == lst[4]):
        lst[8] = 3
    # Q10
    if (max(ct_lst) - min(ct_lst)) == 3:
        lst[9] = 0
    elif (max(ct_lst) - min(ct_lst)) == 2:
        lst[9] = 1
    elif (max(ct_lst) - min(ct_lst)) == 4:
        lst[9] = 2
    elif (max(ct_lst) - min(ct_lst)) == 1:
        lst[9] = 3
    # Q1
    return lst
    # Q1
print(ans(ans(lst)))