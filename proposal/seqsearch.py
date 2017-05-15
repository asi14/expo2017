def sequentialSearch(test, arr):
	output = -1
	count = 0
	run = True
	#the method ieterates through the function
	#demonstrates complexity O(n)
	while run and count < len(arr):
		if arr[count] == test:
			output = count
			run = False
		else:
			count+=1
	return output
