class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = []
        for i in range(numRows):
            if i == 0: lst.append([1])
            else: 
                lst_l = lst[i-1] + [0]
                lst_r = [0] + lst[i-1]
                lst_m = []
                for i in range(i+1):
                    lst_m.append(lst_l[i] + lst_r[i])
                lst.append(lst_m)
        return lst
