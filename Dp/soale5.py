
# Function to find the longest subarray
def longestAlternatingSubarray(a, n):
     
    # Length of longest alternating
    longest = 1
    cnt = 1
 
    # Iterate in the array
    i = 1
    while i < n:
 
        # Check for alternate
        if (a[i] * a[i - 1] < 0):
            cnt = cnt + 1
            longest = max(longest, cnt)
         
        else:
            cnt = 1
        i = i + 1
     
    return longest
 
# Driver Code
b=[]
Mistress_Ghazal=[3,2,1,4,5,1,2,8]
for i in range(len(Mistress_Ghazal)-1):
    b.append(Mistress_Ghazal[i+1]-Mistress_Ghazal[i])
c=len(b)

a = [ -5, -1, -1, 2, -2, -3 ]
n = len(a)
 
# Function to find the longest subarray
print(longestAlternatingSubarray(b, c))
 
# This code is contributed
# by shashank_sharma