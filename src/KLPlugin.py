import numpy as np


def KLPlugin(freqs1, freqs2, unit="log"):
    freqs1 = np.array(freqs1).astype(float)
    freqs2 = np.array(freqs2).astype(float)

    freqs1 = freqs1/np.sum(freqs1)
    freqs2 = freqs2/np.sum(freqs2)

    freqs1 = freqs1[freqs1 > 0]
    freqs2 = freqs2[freqs2 > 0]

    LR = np.log(freqs1/freqs2)
    KL = np.sum(freqs1*LR)

    if unit == "log2":
        KL = KL/np.log(2)

    if unit == "log10":
        KL = KL/np.log(10)


    return KL



def CHI2Plugin(freqs1, freqs2, unit="log"):
    freqs1 = np.array(freqs1).astype(float)
    freqs2 = np.array(freqs2).astype(float)


    freqs1 = freqs1/np.sum(freqs1)
    freqs2 = freqs2/np.sum(freqs2)

    chi2 = sum(  np.power(freqs1-freqs2, 2)/freqs2)

    if unit == "log2":
        chi2 = chi2/np.log(2)

    if unit == "log10":
        chi2 = chi2/np.log(10)

    return chi2


