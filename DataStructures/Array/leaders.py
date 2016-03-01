# Write a function to print all the leaders in the array
# A leader is that element which is greater than all the elements on the right side

def find_leaders(arr):
	i = len(arr)-1
	leaders = []
	while i>=0:
		if i == len(arr)-1 or arr[i] > leaders[-1]:
			leaders.append(arr[i])
		i -= 1
	return leaders
	
if __name__ == '__main__':
	arr = [11,10,9,1,2,3,4,6,5,7,8]
	print 'Leaders are', find_leaders(arr)
