def code(coins, value):
    if value < 0:
        return float('inf')
    elif ready[value]:
        return ans[value]

    else:
        smallest = float('inf')
        temp = []
        for each in coins:
            if smallest > code(coins, value-each):
                temp.append(each)
            smallest = min(code(coins, value-each)+1, smallest)

        ready[value] = True
        ans[value] = smallest
        sets[value] = temp[:]
        return smallest
    
if __name__ == '__main__':
    ready = [False]*251; ready[0] = True
    ans = [ 0 for x in range(251) ]
    sets = [ [] for x in range(251) ]
    x = code([1,3,4], 250)
    print(ans)
    print(sets[10])


















   
    
