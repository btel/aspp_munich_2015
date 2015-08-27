#!/usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from scipy import io
from pyNeuro.analysis import calc_corr_coef

if __name__ == "__main__":

    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('mat_file')
    parser.add_argument('--save')
    
    args = parser.parse_args()

    data = io.loadmat(args.mat_file)
    spike_times = data['spikeTimes'][0]

    corr_coefs = []
    for i, spt1 in enumerate(spike_times[:-1]):
        for spt2 in spike_times[i+1:]:
            r = calc_corr_coef(spt1[0], spt2[0])
            corr_coefs.append(r)

    if args.save:
        np.savez(args.save, corr_coefs = corr_coefs)
    else:
        plt.hist(corr_coefs, 100)
        plt.show()
