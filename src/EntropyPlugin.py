import numpy as np

def Plugin(freqs, unit="log"):
    freqs = np.array(freqs).astype(float)
    freqs = freqs/np.sum(freqs)


    freqs = freqs[freqs>0]
    H = -np.sum(freqs * np.log(freqs))

    if unit == "log2":
        H= H/np.log(2)

    if unit == "log10":
        H = H/np.log(10)

    return H
