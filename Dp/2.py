
MAX = 300
#array baraye zakhire sazi subproblem ha
dp = [[0 for i in range(MAX)] for i in range(MAX)]

def minimum(m, n):
    # Halate khas 13x11
    if n == 13 and m == 11:
        return 6
    if m == 13 and n == 11:
        return 6
 
    #Moraba ast
    if m == n:
        return 1
 
    # agar javab ghablan hesab shode bood return mishavad
    if dp[m][n] != 0:
        return dp[m][n]
 
    # Mostatil be do bakhsh taghsim shode va bakhshe koochaktar 
    # baraye tamame farakhani haye baz gashti yaft shode ast
    for i in range(1, m//2+1):
 
        # the minimum answer for horizontal cut
        horizontal_min = min(minimumSquare(i, n) +
                             minimumSquare(m-i, n), horizontal_min)
    for j in range(1, n//2+1):
 
        # the minimum answer for vertical cut
        vertical_min = min(minimumSquare(m, j) +
                           minimumSquare(m, n-j), vertical_min)
 
    # Minimum of the vertical cut or horizontal
    dp[m][n] = min(vertical_min, horizontal_min)
    return dp[m][n]
 