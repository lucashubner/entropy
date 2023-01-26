import numpy as np
import KLPlugin
import CHI2Plugin


def Chi2IndepPlugin(freqs2d, unit="log"):
    freqs2d = np.matrix(freqs2d)

    freqs_x = np.sum(freqs2d, axis=0)
    freqs_y = np.sum(freqs2d, axis=1)

    freqs_null = np.dot(freqs_x, freqs_y)

    MI = KLPlugin(freqs2d, freqs_null, unit)

    return MI




def MiPlugin(freqs2d, unit="log"):
    freqs2d = np.matrix(freqs2d)

    freqs2d = freqs2d/np.sum(freqs2d)) 

    freqs_x = np.sum(freqs2d, axis=0)
    freqs_y = np.sum(freqs2d, axis=1)


    freqs_null = np.dot(freqs_x, freqs_y)


    chi2 = CHI2Plugin(freqs2d, freqs_null, unit)


    return chi2
