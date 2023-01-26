from scipy.stats import chi2
import numpy as np
import KLPlugin
import EntropyEmpirical



def PVTChisqPval(stat, df, unit="log"):
    stat = np.array(stat).astype(float)
    df = np.array(df).astype(float)

    if unit == "log":
        pval = 1 - chi2.cdf(stat,df)

    if unit == "log2":
        pval = 1 - chi2.cdf(stat*np.log(2),df)

    if unit == "log10":
        pval = 1 - chi2.cdf(stat*np.log(10),df)

    return pval


def Gstat(y, freqs, unit="log"):
    n = np.sum(y)
    df = len(y) - 1

    stat = n * Chi2Empirical(y, freqs,unit)

    pval = PVTChisqPval(stat, df, unit)

    return { 'stat': stat, 'df': df, 'pval':pval }


def Gstatindep(y2d, unit="log"):
    n = np.sum(y2d)

