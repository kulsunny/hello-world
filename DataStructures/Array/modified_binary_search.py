# Search an element in a rotated and sorted array (O(logn))

import find_pivot
import find_binary_search

def modified_binary_search(arr, l, h, x):
		pivot = find_pivot.findpivot(arr, l, h)
		if x == arr[pivot]:
			return pivot
		elif arr[0] <= x:
			return find_binary_search.binary_search(arr, 0, pivot-1, x)
		return find_binary_search.binary_search(arr, pivot+1, h, x)

if __name__ == '__main__':
	arr = [11,10,9,1,2,3,4,6,5,7,8]
	print 'Element is present at', modified_binary_search(arr, 0, 10, 4)
	
