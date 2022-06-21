# finding the no. of ways to part n no. of items in <= m no. of ways.
# Base cases:
# 1: when m = 0 , then ways = 0
# 2: when n = 1 , then ways = 1
# 3: when m =1 , then ways = 1
# 4: when n,m , then ways = ways(n,m-1) + ways(n-m,m)
# 5: when n-m =0, ways = ways (n,m-1) + 1
def part(n,m):
    if m == 0 or n < 0:
        return 0
    elif n == 1 or m ==1:
        return 1
    elif n-m == 0:
        return part(n,m-1) + 1
    else:
        return part(n,m-1) + part(n-m,m)

print("The no. of ways : " + str(part(0,5)))