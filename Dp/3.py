#rabete bazgashti: f(n) = f(n - 1) + (n - 1) * f(n - 2)
# Time Complexity : O(n) 
# Auxiliary Space : O(n)

def Friends(n):
    #array baraye zakhire meghdare subproblem ha dar Dp approach
    dp=[]
    #o(n)
    for i in range(n+1):
        dp.append(0)

    #o(n)
    for i in range(n + 1):
 
        if(i <= 2):
            dp[i] = i
        else:
            dp[i] = dp[i - 1] + (i - 1) * dp[i - 2]
 
    return dp[n]

n = int(input())
print(Friends(n))