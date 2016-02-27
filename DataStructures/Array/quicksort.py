def quicksort(arr, first, last):
	if first < last:
		i = first
		j = last
		p = first
		while (i<j):
			while arr[i] <= arr[p] and i < last:
				i = i + 1
			while arr[j] > arr[p]:
				j = j - 1
			if i < j:
				print 'swapping', arr[i], arr[j]
				arr[j],arr[i] = arr[i],arr[j]
		print 'swapping', arr[p], arr[j]
		arr[p],arr[j] = arr[j],arr[p]
		quicksort(arr, first, j-1)
		quicksort(arr, j+1, last)
		
if __name__ == '__main__':
	arr = [2,3,1,0,9,4,6,5]
	# [2,0,1,3,9,4,6,5]
	# [1,0,2,3,9,4,6,5]
	quicksort(arr, 0, len(arr)-1)
	print arr
