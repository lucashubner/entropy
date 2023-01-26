import EntropyPlugin
import Chi2Plugin

import numpy as np

def FreqsEmpirical(y):
    return y/np.sum(y)

def EntropyEmpirical(y, unit="log"):
    return EntropyPlugin(FreqsEmpirical(y))


def MiEmpirical(y2d, unit="log"):
    return MiPlugin(FreqsEmpirical(y2d))

def Chi2IndepEmpirical(y2d, unit="log"):
    return Chi2IndepPlugin(FreqsEmpirical(y2d))


def Chi2Empirical(y1, y2, unit="log"):
    return Chi2Plugin(FreqsEmpirical(y2), FreqsEmpirical(y2), unit)

def KLEmpirical(y1, y2, unit="log"):
    return KLPlugin(FreqsEmpirical(y2), FreqsEmpirical(t2), unit)


