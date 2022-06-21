def leastBricks(wall):
    countgap = {0:0}

    
    for r in wall:
        total = 0
        c = r[:-1]
        print(c)
        for b in r[:-1]:
            total = total + b
            countgap[total] = 1 + countgap.get(total,0)
    return len(wall) - max(countgap.values())

print(leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))