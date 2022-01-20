# Python3 program to find Maximum difference 
# between two elements such that larger 
# element appears after the smaller number
  
# The function assumes that there are 
# at least two elements in array. The 
# function returns a negative value if 
# the array is sorted in decreasing 
# order and returns 0 if elements are equal
def maxDiff (arr, n):
      
    # Initialize diff, current 
    # sum and max sum
    diff = arr[1] - arr[0]
    curr_sum = diff
    max_sum = curr_sum
  
    for i in range(1, n - 1):
          
        # Calculate current diff
        diff = arr[i + 1] - arr[i]
  
        # Calculate current sum
        if (curr_sum > 0):
            curr_sum += diff
        else:
            curr_sum = diff
  
        # Update max sum, if needed
        if (curr_sum > max_sum):
            max_sum = curr_sum
    return max_sum
  
# Driver Code
if __name__ == '__main__':
    arr = [80, 2, 6, 3, 100]
    n = len(arr)
          
    # Function calling
    print("Maximum difference is",
                  maxDiff(arr, n))
    arr.remove(max(arr))
    arr.remove(max(arr))
    print("Maximum difference is",
                maxDiff(arr, n-2))
    
  
# This code is contributed 
# by 29AjayKumar