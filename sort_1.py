def quicksort(arr):
    sort(arr, 0, len(arr)-1)

def sort(arr, lo, hi):
    if hi <= lo:
        return
    else:
        j = partition(arr, lo, hi)
        sort(arr, lo, j-1)
        sort(arr, j+1, hi)
		
def partition(arr, lo, hi):
    i = lo #compare value at the first of array
    left = lo+1
    right = hi
    while True:        
        while arr[i] >= arr[left]: #1
            left += 1
            if left == hi: break
        while arr[i] <= arr[right]: #2
            right -= 1
            if right == lo: break
        if left > right: break #3 this 3 part can be > < and >= the same performance
        arr[left], arr[right] = arr[right], arr[left]
		# exch(arr, left, right)
    arr[i], arr[right] = arr[right], arr[i]
	# exch(arr, i, right)
    return right


# def exch(arr, i, j):
	# k = arr[i]
	# arr[i] = arr[j]
	# arr[j] = k

#arr = [7,2,6,1,7,9,0]
arr = [3,9,4,1,6,6,8,3,0]
quicksort(arr)
print(arr)
