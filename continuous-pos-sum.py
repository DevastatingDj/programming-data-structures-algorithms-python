A = [ -1, -1, -1, -1, -1 ]
dp = []
temp_l = []
for each in range(0,len(A)):
    if A[each] > 0:
        temp_l.append(A[each])
    else:
        if temp_l:
            dp.append(temp_l)
            temp_l = []
if temp_l:  
    dp.append(temp_l)

if dp:
    dp.sort(key=lambda x: x[0])
    dp.sort(key=lambda x: len(x), reverse = True)
    dp.sort(key=lambda x: sum(x), reverse = True)

if dp:
    return dp
else:
    return []
