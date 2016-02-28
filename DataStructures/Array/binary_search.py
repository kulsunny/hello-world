# Binary search to find an element (O(logn) complexeity)

def binary_search(arr, l, h, x):
	if l<=h:
		m = l + (h-l)/2
		if arr[m] == x:
			return m
		elif arr[m] > x:
			return binary_search(arr, l, m-1, x)
		else:
			return binary_search(arr, m+1, h, x)
	return None

if __name__ == '__main__':
	arr = [-1,2,3,4,6,5,7,8,9]
	print 'Element is present at', binary_search(arr, 0, 8, 0)
