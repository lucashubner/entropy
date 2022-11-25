import numpy as np

def ChaoShen(y, unit ="log"):
    xy = np.array(y)

    xy = xy[xy > 0]

    n = np.sum(xy)
    n = float(n)

    p = xy/n 

    f1 = np.sum ( xy == 1 )

    if( f1 == n ):
        f1 = n-1

    C = 1 - f1/n

    pa = C*p
   
    la = 1 - np.power(1-pa, n)

    H = -np.sum(pa * np.log(pa) /la )

    if unit == "log2":
        H = H/np.log(2)
    if unit == "log10":
        H = H/np.log(10)

    return H
