# Given an array which contains all elements occuring even number of times except one 
# WAF to find that element
# This would work if there is one odd occuring element, otherwise we will have to use dict

def find_odd_occuring_element(arr):
	x = arr[0]
	for i in xrange(len(arr)-1):
		x = x^arr[i+1]
	return x

if __name__ == '__main__':
	arr = [1,2,1,3,2,3,2,2,3,3,4,5,4]
	print 'Odd occuring element is', find_odd_occuring_element(arr)
