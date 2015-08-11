#!/usr/bin/env python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
from scipy import io

def calc_corr_coef(spikes1, spikes2, bin_size=5):
    idx1 = np.searchsorted(spikes1, spikes2)
    idx2 = np.searchsorted(spikes1, spikes2 + bin_size)
    n_coincidences = np.sum(idx2 - idx1)
    r = n_coincidences / np.sqrt(len(spikes1) * len(spikes2))
    return r

if __name__ == "__main__":

    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('mat_file')
    
    args = parser.parse_args()

    data = io.loadmat(args.mat_file)
    spike_times = data['spikeTimes'][0]

    corr_coefs = []
    for i, spt1 in enumerate(spike_times[:-1]):
        for spt2 in spike_times[i+1:]:
            r = calc_corr_coef(spt1[0], spt2[0])
            corr_coefs.append(r)
