#!/usr/bin/env python
#coding=utf-8

import numpy as np


def bin_spikes(spikes, bin_size, tmin=None, tmax=None):
    """Bin spikes."""

    if tmax is None:
        tmax = spikes[-1] 
    if tmin is None:
        tmin = spikes[0] 
    bins = np.arange(tmin, tmax, bin_size)
    left = np.searchsorted(spikes, bins[:-1])
    right = np.searchsorted(spikes, bins[1:], side='right')
    n = right - left
    return bins, n 

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

    if len(spikes1) == 0 or len(spikes2) == 0:
        return 0

    tmin = min((spikes1[0], spikes2[0]))
    tmax = max((spikes1[-1], spikes2[-1]))

    bins, counts1 = bin_spikes(spikes1, bin_size, tmin = tmin, tmax = tmax)
    _, counts2 = bin_spikes(spikes2, bin_size, tmin = tmin, tmax = tmax)
    r = np.corrcoef(counts1, counts2)
    
    return r[0,1]
