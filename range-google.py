#LCS

def LCS(A):
    ans = [0 for x in range(len(A))]
    ans[0] = 1
    current = A[0]
    for i in range(1,len(A)):
        if A[i] > current:
            ans[i] = ans[i-1] + 1
            current = ans[i]
        else:
            ans[i] = ans[i-1]
    return ans


if __name__ == '__main__':
    A = [6,2,5,1,7,4,8,3]
    ans = LCS(A)
    print( ans )
