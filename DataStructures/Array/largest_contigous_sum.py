# Finds the largest contigous sum in an array
# Handles all negative numbers as well

def find_largest_contigous_sum(arr):
	max = 0
	sum = 0
	i = 0
	while i < len(arr):
		if i == 0 or sum+arr[i] > arr[i]:
			sum += arr[i]
		else:
			sum = arr[i]
		if i == 0 or sum >= max:
			max = sum
		else:
			sum = 0
		i += 1
	return max

if __name__ == '__main__':
	arr = [-2,2,-2,4,-4,4,4,-4,2,-2,2]
	arr = [-2,2,3]
	arr = [-2, -1, 1]
	print 'largest contigous sum is', find_largest_contigous_sum(arr)
