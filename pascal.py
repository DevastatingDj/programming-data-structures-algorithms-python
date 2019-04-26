import math
n = int(input())
ans = []

for i in range(0, n+1):
    l = []
    for j in range(0, i+1):
        a = math.factorial(i)
        b = math.factorial(j)
        c = math.factorial(i-j)
        e = a // int(b*c)
        l.append(e)
    ans.append(l)

# Display
x = n
for each in ans:
    string = ''
    for ele in each:
        string = string+str(ele)+'  '
    for j in range(x, 0, -1):
        string = '  ' + string
    x = x - 1
    string.strip()
    print(string)
