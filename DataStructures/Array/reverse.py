# Reverse an array

def reverse(arr, l, h):
	if l < h: 
		arr[l], arr[h] = arr[h], arr[l]
		reverse(arr, l+1, h-1)
	return arr

if __name__ == '__main__':
	arr = [11,10,9,1,2,3,4,6,5,7,8]
	print 'Reverse array is', reverse(arr, 0, 10)
	
