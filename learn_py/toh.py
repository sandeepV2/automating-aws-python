
def toh(n, a, b, c):

    if (n == 1):
        print 'move 1 from %s to %s'%(a,c)
        return
    
    toh(n-1, a, c, b)
    print 'move %s from %s to %s'%(n, a , c)
    toh(n-1, b, a, c)


toh(3, 'a', 'b', 'c')
