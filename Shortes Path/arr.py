def minCostJumpsDP(arr, k):
	
	# x = [sys.maxsize] * (size)
	Sum = [1000000 for i in range(len(arr) + 1)]

	# Base case
	Sum[0] = 0

	# For every element relax every reachable
	# element ie relax next k elements
	for i in range(len(arr)):
		j = i+1
		while(j<i + k+1 and j < len(arr)):
			Sum[j] = min(abs(arr[j] - arr[i])+Sum[i] , Sum[j])
			j += 1
		
	
	return Sum[len(Sum) - 1]

# Driver Code
if __name__ == "__main__":

	input_ = [83, 26, 37, 35, 33, 35, 56]
	print(minCostJumpsDP(input_, 3))
	
# This code is contributed by Rituraj Jain
