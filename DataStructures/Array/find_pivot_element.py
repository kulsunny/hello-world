# Modified binary search - A sorted array is rotated n times, find the element on which the array is rotated
# Pivot element is for which the next element is smaller

def findpivot(arr,l,h):
	if l<=h:
		m = l + (h-l)/2
		if arr[m] > arr[m+1]:
			return m
		elif arr[m] < arr[m-1]:
			return m-1
		elif arr[l] > arr[m]:
			return findpivot(arr,l,m-1)
		else:
			return findpivot(arr,m+1,h)

if __name__ == '__main__':
	arr = [11,10,9,1,2,3,4,6,5,7,8]
	print 'Pivot is present at', findpivot(arr, 0, 10)
