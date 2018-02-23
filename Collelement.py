def colel(lst,l,n):
   if n == 0:
       print(l)
       return 
   colel(lst,l,n-1)
   l.append(lst[n-1])
   colel(lst,l,n-1)
   l.pop()
lst = [1,2,3]
l = []
n = 3
colel(lst, l, n)
