def queen (bd,N):
    lst1 = []
    lst2 = []
    for i in range(N):
        for j in range(N):
            if (i-j) in lst1 or (i+j) in lst2: return
            lst1.append(i-j)
            lst2.append(i+j)
            bd[i] = j  #一行i里存一个列值j,每行放的皇后唯一,且位置由j确定
            
            print(bd)
bd = [0 for i in range(4)]            
#bd = (for i in range(4), for j in range(4))
#bd = [[0 for i in range(4)] for j in range(4)]
queen(bd,4)
