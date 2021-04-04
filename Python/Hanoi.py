def move(a,b):
    print("move from " + a + " to " + b)
#move("A","B")

#def moveVia(a,b,c):
#    move(a,b)
#    move(b,c)
#
#moveVia("A","B","C")

def Hanoi(n,f,h,t):
    if n == 0:
        pass
    else:
        Hanoi(n-1,f,t,h)
        move(f,t)
        Hanoi(n-1,h,f,t)
Hanoi(5,"A","B","C")





















