
def mergeHelp(left,right,arr):
	i = 0 
	j = 0
	k = 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			arr[k] = left[i]
			k += 1
			i += 1

		else:
			arr[k] = right[j]
			k += 1
			j += 1

	while i < len(left):
		arr[k] = left[i]
		k += 1
		i += 1

	while j < len(right):
		arr[k] = right[j]
		k += 1
		j += 1

def mergeSort(arr):
	mid = len(arr) // 2

	if len(arr) == 1 or len(arr) == 0:
		return 

	left = arr[0:mid]
	right = arr[mid:]

	mergeSort(left)
	mergeSort(right)

	mergeHelp(left,right,arr)


if __name__ == '__main__':

	arr = [1,5,0,3,2,7]
	mergeSort(arr)
	print(arr)


