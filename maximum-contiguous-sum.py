A = [-2,1,-3,4,-1,2,1,-5,4]
dp = [0 for x in range(0,len(A))]
dp[0] = A[0]
for i in range(1, len(A)):
    dp[i] = max(dp[i-1] + A[i], A[i])
print(max(dp))
