def cost(arr, k):
	for i in range(len(arr)):
		j=i+1
		while(j<=i+k and j<len(arr)):
			res[j] = min(abs(arr[i] - arr[j])+res[i],res[j])
			j += 1
		
	return res[len(arr) - 1]

if __name__ == "__main__":
	inp=input().split()
	data=list(map(int, input().split()))
	n,k=(int(inp[0]),int(inp[1]))

	res=[1000000 for i in range(n+1)]
	res[0]=0
	
	
	
	
	if(len(data)!=n):
		quit()

	print(cost(data,k))
	

