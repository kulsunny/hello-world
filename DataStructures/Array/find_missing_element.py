def find_missing_integer(arr):
	n = len(arr) + 1
	sum_n = (n*(n+1))/2
	sum = 0
	for i in range(n-1):
		sum += arr[i]
	return sum_n - sum

if __name__ == '__main__':
	arr = [1,2,3,4,5,7,8,9]
	print 'Missing element is', find_missing_integer(arr)
