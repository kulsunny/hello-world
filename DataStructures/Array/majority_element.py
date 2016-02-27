# Majority element is that element which exists at least n/2 times in an array
# Write a function to check if such element exists or not

def find_majority_element(arr):
	result = {}
	for i in range(len(arr)):
		if result.get(arr[i]) > len(arr)/2:
			return arr[i]
		else:
			result[arr[i]] = result.get(arr[i],0) + 1
	return None


if __name__ == '__main__':
	arr = [2,2,2,4,4,4,4,4,2,2,2]
	print 'majoity element is', find_majority_element(arr)
	
