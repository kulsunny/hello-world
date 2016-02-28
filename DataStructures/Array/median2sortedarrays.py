# Calculate the median of 2 sorted arrays
# 

def getmedian(arr1,arr2):
	i = len(arr1)-1
	j = len(arr2)-1
	arr3 = []
	while i >= 0 and j >=0:
		if arr2[j] > arr1[i]:
			arr3.append(arr2[j])
			j -= 1
		else:
			arr3.append(arr1[i])
			i -= 1
		if len(arr3) == (len(arr1)+len(arr2)+1)/2:
			print 'median is', arr3[-1]
			break
			
if __name__ == '__main__':
	arr1 = [1,2,3,5,6]
	arr2 = [0,4,10,20]
	getmedian(arr1,arr2)
