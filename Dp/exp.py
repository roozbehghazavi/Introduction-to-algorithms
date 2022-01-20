rows, cols = (1000, 2)
LAS = [[0 for i in range(cols)] for j in range(rows)]

  
for i in range(1000) :
    for j in range(2) :
        LAS[i][j] = False
  
def solve(arr, n, i, pos) :
  
    # Base Case 
    if (i == n) :
        return 0; 
  
    if (LAS[i][pos]) :
        return LAS[i][pos]; 
  
    inc = 0; exc = 0; 
  
    # If current element is 
    # positive and pos is true 
    # Include the current element 
    # and change pos to false 
    if (arr[i] > 0 and pos == True) :
        pos = False; 
  
        # Recurr for the next 
        # iteration 
        inc = 1 + solve(arr, n, i + 1, pos); 
  
    # If current element is 
    # negative and pos is false 
    # Include the current element 
    # and change pos to true 
    elif (arr[i] < 0 and pos == False) :
        pos = True; 
  
        # Recurr for the next 
        # iteration 
        inc = 1 + solve(arr, n, i + 1, pos); 
      
    # If current element is 
    # excluded, reccur for 
    # next iteration 
    exc = solve(arr, n, i + 1, pos); 
  
    LAS[i][pos] = max(inc, exc); 
  
    return LAS[i][pos]; 
  
# Driver's Code 
if __name__ == "__main__" : 
    a=[3,2,1,4,5,1,2,8]
    b=[]
    for i in range(len(a)-1):
        b.append(a[i+1]-a[i])
    n = len(b)
  
    # Print LAS 
    print(max(solve(b, n, 0, 0), solve(b, n, 0, 1)))
      
