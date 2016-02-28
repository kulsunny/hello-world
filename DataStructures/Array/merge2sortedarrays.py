# Merge an array of size n into an array of size m+n which already has m elements
# Both arrays are sorted

def merge2sortedarrays(arr1, arr2, m, n):
	big_array_index= m+n-1
	i = m-1
	j = n-1
	while j >= 0 and i >= 0:
		if arr2[j] >= arr1[i]:
			arr1[big_array_index] = arr2[j]
			big_array_index -= 1
			j -= 1
		else:
			arr1[big_array_index] = arr1[i]
			big_array_index -= 1
			i -= 1
	
	while j > -1:
		arr1[big_array_index] = arr2[j]
		j -= 1
		big_array_index -=1
	
if __name__ == '__main__':
	arr1 = [1,2,3,5,6,None,None,None,None]
	arr2 = [0,4,10,20]
	merge2sortedarrays(arr1,arr2,5,4)
	print 'Modified array1 is', arr1
