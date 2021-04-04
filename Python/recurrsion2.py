def route(n,m,x = {}):
    key = m + n
    if key in x:
        return x[key]
    if n == 1 or m == 1:
        return 1
    elif n==0 or m == 0:
        return 0
    else:
        x[key] = route(n-1,m) + route(n,m-1)
        return x[key]
print("Total no. of paths : " + str(route(20,30)))