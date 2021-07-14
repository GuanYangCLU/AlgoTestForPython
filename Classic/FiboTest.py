def fibo(dic, n):
     global counter
     counter += 1
     if (n in dic): 
     	return dic[n]
     if (n<2): 
     	dic[n] = n 
     	return dic[n]
     else: 
     	temp = fibo(dic, n-1) + fibo(dic, n-2)
     	dic[n] = temp
     	return dic[n]

dic = {}
counter = 0
print (fibo(dic, 10), counter)