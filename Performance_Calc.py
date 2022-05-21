def Performance(kd, kr, discrep):
    import numpy as np

    elo_multi = 2/(1+np.exp(-2.5*discrep/1000))
    avg_kr = 0.72
    avg_kd = 1
    kr_multi = np.tanh(2*(kr-avg_kr)) + 1
    kd_multi = np.tanh((kd-avg_kd)/2) + 1

    return elo_multi * kr_multi * kd_multi