# Program for array rotation by d elements

def array_rotation(arr, d):
	arr_rotated = list(arr) # Makes a copy,changing arr_rotated won't change arr
	i = 0
	j = 0
	while i <len(arr_rotated) and i+d < len(arr):
		arr_rotated[i] = arr[i+d]
		i += 1
	while j < d:
		arr_rotated[i+j] = arr[j]
		j += 1
	return arr_rotated

if __name__ == '__main__':
	arr = [11,10,9,1,2,3,4,6,5,7,8]
	print 'Rotated array is', array_rotation(arr, 2)
