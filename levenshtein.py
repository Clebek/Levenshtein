import numpy as np

def naive_lev(a: str, b: str):
    if len(a) == 0:
        return len(b)
    if len(b) == 0:
        return len(a)
    if a[0] == b[0]:
        return naive_lev(a[1:],b[1:])
    return 1 + min(naive_lev(a[1:],b),naive_lev(a,b[1:]),naive_lev(a[1:],b[1:]))

def lev(a: str,b: str):
    # Implementation of Magnus-Fischer algorithm
    distmat = np.zeros((len(a)+1,len(b)+1))
    
    distmat[0,:] = np.arange(len(b)+1)
    distmat[:,0] = np.arange(len(a)+1)

    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1] == b[j-1]:
                s = 0
            else:
                s = 1
            distmat[i,j] = min(distmat[i-1,j] + 1,
                                distmat[i,j-1] + 1,
                                distmat[i-1,j-1] + s)
    return distmat[-1,-1]
