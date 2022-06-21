def sum(n):
    result = 0
    for i in range(n+1):
        result +=i   
    return result


def sum_rec(n):
    if n == 0:
        return 0
    else:
        return sum_rec(n-1) + n

print(sum_rec(10))  