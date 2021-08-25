def binarySearch(arr,start,end,val):

	mid = (start+end) // 2

	if start > end:
		return -1

	if arr[mid] == val:
		return mid

	elif arr[mid] > val:
		return binarySearch(arr,start,mid-1,val)

	else:
		return binarySearch(arr,mid+1,end,val)


if __name__ == '__main__':

	arr = [10,20,30,40,50]

	print(binarySearch(arr,0,4,200))