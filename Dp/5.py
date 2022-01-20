# Time Complexity: O(n) 
# Auxiliary Space: O(1)
#------------------------------------------------------
# yeki darmion mosbat manfi shodan pas az tafrigh
# haman masale yaftane "Longest alternating subsequence" dar array avalie 
# mibashad pas az algorithm haman soal estefade mikonim.

# sharte alternating subsequence:
#   x1 < x2 > x3 < x4 > x5 < …. xn or 
#   x1 > x2 < x3 > x4 < x5 > …. xn
#------------------------------------------------------
def Longest(arr, n):
    increase = 1
    decrease = 1
     
    for i in range(1,n):
       
        if (arr[i] > arr[i-1]):
            increase = decrease + 1

        elif (arr[i] < arr[i-1]):
            decrease = increase + 1
             
    
    return max(increase, decrease)
 
n=int(input())
data=input()
data=list(map(int, data.split()))

if(n!=len(data)):
    quit()

print(Longest(data, n))