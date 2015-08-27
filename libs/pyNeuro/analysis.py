#!/usr/bin/env python
#coding=utf-8

import numpy as np

def calc_corr_coef(spikes1, spikes2, bin_size=5):
    """Calculate correlation between two spike trains.
    
    Parameters
    ----------
    spikes1 : array_like
    spikes2 : array_like
        Arrays of spike times to correlate (in miliseconds)
        
    bin_size : float
        Binning used for calculating the correlation.
        
    Returns
    -------
    
    r : float
        Value of Pearson correlation coefficient between the spike times."""


    idx1 = np.searchsorted(spikes1, spikes2)
    idx2 = np.searchsorted(spikes1, spikes2 + bin_size)
    n_coincidences = np.sum(idx2 - idx1)
    r = n_coincidences / np.sqrt(len(spikes1) * len(spikes2))
    return r
