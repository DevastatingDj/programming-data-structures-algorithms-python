def permute(s, n):
    global size, ans
    
    if len(s) == size:
        ans.append(s)
        return
    
    else:

        # Select every element in n and choose and unchoose it

        for i in range(0,len(n)):
            # Choose
            s.append(n[i])
            temp1 = s[:] ; temp2 = n[:]
            temp2.remove(n[i])
            
            # Process
            permute(temp1 , temp2)

            # Unchoose
            s.remove(n[i])
        
nums = [1,2,3]

size = len(nums)
ans = []
permute([], n = nums)
print(ans)
