#test file trash, just do anything here

lst = [0 for i in range(3)]
lst_rt = []
def comb(lst):
    # lst_rt = []
    for j in range (4):
        lst[0] = j
        
        if len(lst) == 1:
            print(lst_rt)
            return lst_rt
        else:
                
            sub_lst = lst[1:]               
            lst_rt.append(lst[0])
            lst.pop(0)
            comb(lst)
    
        
       
            
            # print(lst_rt,'2')
    print(lst_rt)
        # return lst
def fvck(lst):
    count = 0
    for i1 in range(4):
        for i2 in range(4):
            for i3 in range(4):
                lst = [i1,i2,i3]
                count += 1
                print(lst,count)
fvck(lst)
