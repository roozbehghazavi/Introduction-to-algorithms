def Prefix(arr):
    prefix[0] = arr[0]
 
    for i in range(1, n):
        prefix.append(abs(prefix[i - 1] - arr[i]))
        


if __name__ == "__main__":
    inp=input()
    data=list(map(int, input().split()))
    data.sort()

    n,k=(int(inp[0]),int(inp[2]))
    prefix=[0]
    
    if(len(data)!=n):
        quit()
    
    Prefix(data)

    print(prefix[len(prefix)-1])



