


def read_str(str):
    read_dic = dict()
    for i in str:
        if i not in read_dic:
            read_dic[i] = 1
        else:
            read_dic[i] += 1
    return read_dic
 
def check_str(str):
    pos = [False for i in range(len(str))]
    c_lst = list(str)
    for i in range(len(str)):
        if read_dic[c_lst[i]] == 1:
            pos[i] = True
            if i == 0:
                pass
            elif i > 0:
                if pos[i-1] == True:
                    pass
                elif c_lst[i-1] < c_lst[i]:
                    
                check_str(str[i-1:]
        elif read_dic[c_lst[i]] > 1:
            
    # str_index = 0
    # for i in str:
        # if read_dic[i] > 1:
            # str_index += 1
            # check_str(str[i:])
        # elif read_dic[i] == 1:
            # pos[str_index] = True
            # if (str_index == 0)||(read_dic[i-1] == 1):
                # str_index += 1
            # else:
                # str_index -= 1
                # if i-1 > i:
                    # str = str[:i-2] + str[i:]
                    # str_index -= 1
                # else:
                    # pos[str_index] = True
                
            
                
                
            

 
str1 = 'bcabc'
print (read_str(str1))