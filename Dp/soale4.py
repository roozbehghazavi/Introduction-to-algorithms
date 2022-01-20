# DP Approach
# Time Complexity:O(m*n)
# Space Complexity:O(m*n)

def MED(str1, str2, m, n):
	if(m>20 or n>20):
		quit()
		
	# yek array baraye zakhire kardane natije subproblem ha.
	dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

	# Por kardane d[][] be shive bottom up:
	for i in range(m + 1):
		for j in range(n + 1):

			# Agar str1 khali bood pas bayad mohtavaye str2
			# betore kamel dar str1 darj shavad.
			if i == 0:
				dp[i][j] = j 

			# Agar str2 khali bood pas bayad mohtavate str1
			# kamel delete shavad.
			elif j == 0:
				dp[i][j] = i 

			# Agar harfe akhare str1 va str2 yeksan bood ignore mikone 
			# va be sorate bazgashti baghie str ro migarde.
			elif str1[i-1] == str2[j-1]:
				dp[i][j] = dp[i-1][j-1]

			# Agar hafte akhare str1 va str2 motafavet bood tamame
			# halat(Replace,Insert,Remove) ro dar nazar gerefte va minimum cost ro bedast miarim
			# Replace Cost=2, Insert or Remove Cost=1
			else:
				if(min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])==dp[i-1][j-1]):
					dp[i][j]=2+dp[i-1][j-1]
				else:
					dp[i][j]=1+min(dp[i][j-1],dp[i-1][j])

				# dp[i][j-1]   # Insert
				# dp[i-1][j]   # Remove
				# dp[i-1][j-1] # Replace

	return dp[m][n]

str1 = str(input())
str2 = str(input())
print(MED(str1,str2,len(str1),len(str2)))

