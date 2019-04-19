import copy
a = "Hello World"
def double_word(w):
    c = []
    w_lst = list(w)
    for i in range(0, len(w_lst), 2):
        if i == len(w_lst)-1:
            c.append(str(w_lst[i]))
            break
        else:
            c.append(str(w_lst[i]) + str(w_lst[i+1]))
    print(c)
    
double_word(a)


a_lst = list(a)
c = []
d = []
def rec_double(w_lst, c):
    # c = []
    # w_lst = list(w)
    if len(w_lst) < 1:
        print("0",c)
        d = c + []
        print (d)
        return d
    elif len(w_lst) == 1:
        print("1",c)
        c.append(str(w_lst.pop(0)))
        rec_double(w_lst, c)
    else:
        print("2",c)
        c.append(str(w_lst.pop(0)) + str(w_lst.pop(0)))
        rec_double(w_lst, c)

print(rec_double(a_lst, c))



step = 2

def cool_db(w, step):
    return [w] if len(w) <= step else [w[:step]] + cool_db(w[step:], step)
    
print (cool_db(a, step))


def easyDb(w): #only for 2
    lst_1 = w[::2]
    lst_2 = w[1::2]
    if len(lst_2) < len(lst_1):
        lst_2 += ' '
        tail = True
    #print (lst_1,lst_2)
    zipped = zip(lst_1,lst_2)
    lst = list(zipped)
    for i in range((int)(len(w)/2)+1):
        lst[i] = "".join(lst[i])  # tuple cannot be subsripted, must transfer to list
    if tail == True:
        lst[-1] = lst[-1].rstrip()
        tail = False
    return lst
# a = "Hello World"  
print (easyDb(a))