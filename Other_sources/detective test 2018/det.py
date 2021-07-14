# import random
# meta code for detect, keep it
def ans():
    # lst = [random.randint(0,3) for i in range(10)]
    ct_lst = [lst.count(0),lst.count(1),lst.count(2),lst.count(3)]
    if (  (lst[4] == 2 and lst[1] == 0) or (lst[4] == 3 and lst[1] == 1) or (lst[4] == 0 and lst[1] == 2) or (lst[4] == 1 and lst[1] == 3)  ) and \
    (  ((lst[2] not in [lst[1],lst[3],lst[5]]) and lst[2] == 0) or ((lst[5] not in [lst[1],lst[3],lst[2]]) and lst[2] == 1) or \
    ((lst[1] not in [lst[2],lst[3],lst[5]]) and lst[2] == 2) or ((lst[3] not in [lst[1],lst[2],lst[5]]) and lst[2] == 3)  ) and \
    (  (lst[0] == lst[4] and lst[3] == 0) or (lst[1] == lst[6] and lst[3] == 1) or (lst[0] == lst[8] and lst[3] == 2) or (lst[5] == lst[9] and lst[3] == 3)  ) and \
    (  (lst[7] == lst[4] and lst[4] == 0) or (lst[3] == lst[4] and lst[4] == 1) or (lst[8] == lst[4] and lst[4] == 2) or (lst[6] == lst[4] and lst[4] == 3)  ) and \
    (  ((lst[7] == lst[1]) and (lst[7] == lst[3]) and lst[5] == 0) or ((lst[7] == lst[0]) and (lst[7] == lst[5]) and lst[5] == 1) or \
    ((lst[7] == lst[2]) and (lst[7] == lst[9]) and lst[5] == 2) or ((lst[7] == lst[4]) and (lst[7] == lst[8]) and lst[5] == 3)  ) and \
    (  (lst.count(2) == min(ct_lst) and lst[6] == 0) or (lst.count(1) == min(ct_lst) and lst[6] == 1) or \
    (lst.count(0) == min(ct_lst) and lst[6] == 2) or (lst.count(3) == min(ct_lst) and lst[6] == 3)  ) and \
    (  (((abs(lst[6] - lst[0]) == 2) or (abs(lst[6] - lst[0]) == 3)) and lst[7] == 0) or (((abs(lst[4] - lst[0]) == 2) or (abs(lst[4] - lst[0]) == 3)) and lst[7] == 1) or \
    (((abs(lst[1] - lst[0]) == 2) or (abs(lst[1] - lst[0]) == 3)) and lst[7] == 2) or (((abs(lst[9] - lst[0]) == 2) or (abs(lst[9] - lst[0]) == 3)) and lst[7] == 3)  ) and \
    (   ((lst[0] != lst[5]) == (lst[5] == lst[4]) and lst[8] == 0) or ((lst[0] != lst[5]) == (lst[9] == lst[4]) and lst[8] == 1) or \
    ((lst[0] != lst[5]) == (lst[1] == lst[4]) and lst[8] == 2) or ((lst[0] != lst[5]) == (lst[8] == lst[4]) and lst[8] == 3)  ) and \
    (  ((max(ct_lst) - min(ct_lst)) == 3 and lst[9] == 0) or ((max(ct_lst) - min(ct_lst)) == 2 and lst[9] == 1) or \
    ((max(ct_lst) - min(ct_lst)) == 4 and lst[9] == 2) or ((max(ct_lst) - min(ct_lst)) == 1 and lst[9] == 3)  ):

        return lst + ['right']
    else:
        return lst + ['wrong']
print (ans())

lst = [0 for i in range(10)]
def comb(lst):

    for i in range(len(lst)):
        for j in range (4):
            if lst == []:
                return lst
            else :
                lst[i] = j
                sub_lst = lst[1:]               
                lst = lst[i] + comb(sub_lst)
            