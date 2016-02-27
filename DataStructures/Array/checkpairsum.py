# check for pair in a whose sum is x

import quicksort

def checkpairsum(arr, x):
	result = {}
	for i in xrange(len(arr)):
		j = i+1
		list = []
		while j < len(arr):
			if x == arr[i] + arr[j]:
				list.append(j)
			j = j+1
		result[i] = list
	
	return result

def checkpairsumaftersorting(arr, x):
	quicksort.quicksort(arr, 0, len(arr)-1)
	print arr
	i = 0
	j = len(arr)-1
	while (i<j):
		if arr[i]+arr[j] > x:
			j -= 1
		if arr[i]+arr[j] < x:
			i += 1
		if arr[i]+arr[j] == x:
			return True
	return False
	
if __name__ == '__main__':
	arr = [2,3,5,0,-3,1,8,6,7,2]
	result = checkpairsum(arr, 5)
	for first, second in result.iteritems():
		print 'first value:', first, 'second value(s):', second
	
	print checkpairsumaftersorting(arr, 5)
