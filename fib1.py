#def feb(x,t):
 #   y = []
  # n=1
   # y.append(m)
    #y.append(n)
    #for i in range(x):
     #   y.append(y[i]+y[i+1])
      #  if len(y) == x:
       #     break
#     print("INVALID POSITION")
 #   elif x == t:
  #      return y[t-1]
   # else:
    #    return (y[t])  

#print(feb(50,50))

#def fib(n):
#    if n <=2:
#        return 1
#    else:
#        return fib(n-1) + fib(n-2)
#print(fib(50))


def fib(n,memo = {}):
    if n <= 2:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

print(fib(7))